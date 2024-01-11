#!/usr/bin/env python3
"""Reviews"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    name_of_class = 'Review'
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
