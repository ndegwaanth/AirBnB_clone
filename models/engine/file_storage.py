#!/usr/bin/env python3
"""this is a python script"""

import os
import json


class FileStorage:
    """serialized instances to json and viseversa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __object"""
        return self.__objects

    def new(self, obj):
        """setting the __object to obj having this info class.id"""
        # spec_key = f"{obj.__class__.__name__}.{obj.id}"
        spec_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[spec_key] = obj

    def save(self):
        """serializing the __objects to json file in this file __file_path"""
        object_serialization = {}
        for key, value in self.__objects.items():
            object_serialization[key] = value.to_dict()

        with open(self.__file_path, 'w') as file_content:
            json.dump(object_serialization, file_content)

    def reload(self):
        """deserialize the json file to __objects"""
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.base_model import BaseModel
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    temp = json.load(f)
                    for key, value in temp.items():
                        spec_class = value.get("__class__", "BaseModel")
                        cls_type = self.__objects.get(spec_class, BaseModel)
                        obj = cls_type(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
