#!/usr/bin/env python3
"""State"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name_of_class = 'State'
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_dict(self):
        """return a dictionary representation of State"""
        state_dict = super().to_dict()
        state_dict['name'] = self.name

        return state_dict
