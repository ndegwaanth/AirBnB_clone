#!/usr/bin/env python3
"""amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name_of_class = 'Amenity'
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """return a dictionary representation of Amenity"""
        amenity_dict = super().to_dict()
        amenity_dict['name'] = self.name

        return amenity_dict
