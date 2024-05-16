#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    # Path to the JSON file
    __file_path = "file.json"
    # Dictionary to store objects
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        # Convert objects to dictionary format
        json_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        # Write dictionary to JSON file
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
