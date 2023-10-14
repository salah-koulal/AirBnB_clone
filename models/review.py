#!/usr/bin/python3
"""Defines a class Review  that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing reviews
    of places in the AirBnB clone project.

    Attributes:
        place_id (str): ID of the place being reviewed.
        user_id (str): ID of the user who wrote the review.
        text (str): The review text.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Review.
        """
        super().__init__(*args, **kwargs)
