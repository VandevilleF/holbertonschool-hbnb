#!/usr/bin/env python3
""" Test module for Place
"""
from app.models.place import Place
from app.models.user import User
from app.models.review import Review


def test_place_creation():
    owner = User("Alice", "Smith", "alice.smith@example.com")
    place = Place("Cozy Apartment", "A nice place to stay", 100, 37.7749, -122.4194, owner)

    # Adding a review
    review = Review("Great stay!", 5, place, owner)
    place.add_review(review)

    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"
    print("Place creation and relationship test passed!")


test_place_creation()
