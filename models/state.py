#!/usr/bin/env python3
"""State"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name_of_class = 'State'
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
