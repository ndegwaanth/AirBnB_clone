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

    def to_dict(self):
        """return a dictionary representation of Review"""
        review_dict = super().to_dict()
        review_dict['place_id'] = self.place_id
        review_dict['user_id'] = self.user_id
        review_dict['text'] = self.text

        return review_dict
