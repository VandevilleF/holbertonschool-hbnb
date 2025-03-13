#!/usr/bin/env python3
""" User Module
"""
from app.models.base_model import BaseModel
from app.utils.validators import is_valid_email

REGISTERED_EMAILS = set()


class User(BaseModel):
    """ Class representing a user.
    """
    def __init__(self, first_name, last_name, email, is_admin=False):
        """ Initializes a User instance.
        """
        super().__init__()

        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError(
                "First name and last name must not exceed 50 characters.")
        if not is_valid_email(email):
            raise ValueError("Invalid email format.")
        if email in REGISTERED_EMAILS:
            raise ValueError("This email is already registered.")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []

    def add_place(self, place):
        """ Add a place to the user.
        """
        from app.models.place import Place
        if isinstance(place, Place):
            self.place.append(place)
        else:
            raise ValueError("Invalid: place must be an instance of Place.")
