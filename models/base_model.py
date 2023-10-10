#!/usr/bin/python3

import uuid
import datetime as dt
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = dt.datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = dt.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] (<{}>) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Call save() method of storage"""
        storage.save()
        return self.updated_at

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
