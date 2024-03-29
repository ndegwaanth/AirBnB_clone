#!/usr/bin/env python3
"""this is the python script"""

import uuid
import datetime
from models import storage
from models.engine.file_storage import FileStorage


class BaseModel:
    """define all the common attribute/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """this method print the class name, id and all method in it"""
        # return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(
                class_name,
                self.id,
                {key: getattr(self, key) for key in self.__dict__.keys() if key != '__class__'}
        )

    def save(self):
        """update update_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the particular instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
                dictionary['__class__'] = self.__class__.__name__
                return dictionary
        """return a dictionary containing all the keys
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj"""
