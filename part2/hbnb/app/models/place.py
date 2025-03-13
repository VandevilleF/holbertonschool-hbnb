#!/usr/bin/env python3
""" Place module
"""
from app.models.base_model import BaseModel
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity


class Place(BaseModel):
    """ Class representing a place.
    """
    def __init__(self, title, description, price, latitude, longitude, owner):
        """ Initializes a Place instance.
        """
        super().__init__()

        if len(title) > 100:
            raise ValueError("Title must not exceed 100 characters.")
        if price <= 0:
            raise ValueError("Price must be positive.")

        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Invalid latitude.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Invalid longitude.")

        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = set()

    def add_review(self, review):
        """ Add a review to the place.
        """
        if isinstance(review, Review):
            self.reviews.append(review)
        else:
            raise ValueError("Invalid: rview must be a instance of Review.")

    def add_amenity(self, amenity):
        """ Add a amenity to the place.
        """
        if isinstance(amenity, Amenity):
            self.amenities.append(amenity)
        else:
            raise ValueError("Invalid: amenity must be an instance of Amenity.")
