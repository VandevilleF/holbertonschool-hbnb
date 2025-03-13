#!/usr/bin/env python3
""" Test module for Amenity
"""
from app.models.amenity import Amenity


def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")


test_amenity_creation()
