#!/usr/bin/python3
"""
This file defines  the BaseModel class which will
serve as the base of ou model.
"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        This COnstructor Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())  # Generating a unique id and convert it to a string
        self.created_at = datetime.now()  # Setting created_at to the current datetime
        self.updated_at = datetime.now()  # Setting updated_at to the current datetime

    def __str__(self):
        """
        Returns a string representation of the BaseModel object. __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updating the updated_at attribute with the current datetime. Whenever save method is called.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel object. In other words this process is called Serialization.
        """
        # Creation of a dictionary containing all instance attributes
        obj_dict = self.__dict__.copy()

        # Adding __class__ key with the class name to the dictionary
        obj_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings. We convert the instance(object) into a string for better storage...
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

# Example usage:
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

