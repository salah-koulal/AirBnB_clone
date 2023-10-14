#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """Class for creating state object which inherits
    `BaseModel` properties"""
    name = ""
