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
