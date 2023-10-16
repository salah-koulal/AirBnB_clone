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

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

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
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                dict_objs = json.load(file)
                for key, value in dict_objs.items():
                    cls_name = key.split('.')[0]
                    if cls_name in self.classes():
                        instance = self.classes()[cls_name](**value)
                        self.new(instance)
