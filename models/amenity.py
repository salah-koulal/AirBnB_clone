#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for creating amenities objects which inherits
    `BaseModel` properties"""
    name = ""
