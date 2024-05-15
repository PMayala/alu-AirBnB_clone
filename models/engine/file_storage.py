#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""

import json
import os.path
from models.user import User
from models.base_model import BaseModel

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
        if os.path.exists(self.__file_path):
            # Read JSON file
            with open(self.__file_path, 'r') as f:
                # Load JSON data into dictionary
                json_dict = json.load(f)
                # Loop through dictionary to recreate objects
                for key, obj_dict in json_dict.items():
                    # Split key to get class name and object ID
                    class_name, obj_id = key.split('.')
                    # Get class reference using eval
                    obj_class = eval(class_name)
                    # Create instance of class with dictionary data
                    obj_instance = obj_class(**obj_dict)
                    # Store instance in __objects
                    self.__objects[key] = obj_instance

