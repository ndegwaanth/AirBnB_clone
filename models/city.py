#!/usr/bin/env python3
"""City"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    name_of_class = 'City'
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """return a dictionary representation of City"""
        city_dict = super().to_dict()
        city_dict['state_id'] = self.state_id
        city_dict['name'] = self.name

        return city_dict
