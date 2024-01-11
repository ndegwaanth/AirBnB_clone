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
                    pass
                if key in ['created_at', 'updated_at']:
                    setattr(self, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """this method print the class name, id and all method in it"""
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """update update_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary containing all the keys"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
