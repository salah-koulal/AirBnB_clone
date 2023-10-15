#!/usr/bin/python3
"""Defines a class Base"""
import uuid
import datetime as dt
from models import storage


class BaseModel:
    """The BaseModel class defines common
    attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """ Creates new instances of Base """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, dt.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string represation of class details.

        Returns:
            str: class details
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Call save() method of storage"""
        self.updated_at = dt.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
