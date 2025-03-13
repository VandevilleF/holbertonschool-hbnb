#!/usr/bin/env python3
""" Review module
"""
from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    """ Class representing a review.
    """
    def __init__(self, text, rating, place, user):
        """ Initialize a review instance.
        """
        super().__init__()
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not isinstance(place, Place):
            raise ValueError("Invalid: place must be an instance of Place.")
        if not isinstance(user, User):
            raise ValueError("Owner must be a valid User instance.")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
