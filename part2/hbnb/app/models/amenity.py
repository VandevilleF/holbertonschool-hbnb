#!/usr/bin/env python3
""" Amenity module
"""
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class representing a amenity.
    """
    def __init__(self, name):
        """ Initialize a Amenity instance.
        """
        super().__init__()

        if len(name) > 50:
            raise ValueError("Amenity name must not exceed 50 characters.")
        self.name = name
