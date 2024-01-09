#!/usr/bin/env python3
"""this is a python script"""

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
        spec_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[spec_key] = obj

    def save(self):
        """serializing the __objects to json file in this file __file_path"""
        object_serialization = {}
        for key, value in self.__objects.items():
            object_serialization[key] = value.to_dict()

        with open(self.__file_path, 'w') as file_content:
            json.dumps(object_serialization, file_content)

    def reload(self):
        """deserialize the json file to __objects"""
        try:
            with open(self.__file_path, 'r') as file_content:
                file = json.loads(file_content)
                for key, value in file.items():
                    name_of_class, obj_id = key.split('.')
                    obj = globals()[name_of_class(**value)]
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
