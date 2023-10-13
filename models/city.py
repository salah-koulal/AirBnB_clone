#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """Class for creating city object which inherits
    `BaseModel` properties"""
    state_id = ""
    name = ""
