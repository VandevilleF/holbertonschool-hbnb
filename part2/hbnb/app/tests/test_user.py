#!/usr/bin/env python3
""" Test module for User
"""
from app.models.user import User


def test_user_creation():
    """ Test user creation with good input
    """
    user = User("John", "Doe", "john.doe@exemple.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@exemple.com"
    assert user.is_admin is False
    print("User creation test passed!")


test_user_creation()
