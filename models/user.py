#!/usr/bin/env python3
"""class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """this class inherit the basemodel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, email="", password="", first_name="", last_name="", **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        """return a dictionary representation of user"""
        uset_dict = super().to_dict()
        uset_dict['email'] = self.email
        uset_dict['password'] = self.password
        uset_dict['first_name'] = self.first_name
        uset_dict['last_name'] = self.last_name
        return uset_dict

    def __str__(self):
        """return a string representation of User"""
        return "[User] ({}) {}".format(self.id, self.to_dict())
