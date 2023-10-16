#!/usr/bin/python3
"""Defines a class FileStorage."""
import json
import os


class FileStorage:
    """all method: Returns the object

    new method: updates the dictionary id

    save method: Serializes, or converts Python objects into JSON strings.
    reload method: Deserializes, or converts JSON strings
    into Python objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        Serialize_dict = {}

        for key, value in FileStorage.__objects.items():
            Serialize_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(Serialize_dict, file)

    def reload(self):
        """ Deserializes __objects from the JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'City': City,
               'Amenity': Amenity,
               'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
