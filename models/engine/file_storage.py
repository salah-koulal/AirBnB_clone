#!/usr/bin/python3
"""Defines a class FileStorage."""
import json


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
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key in __class__.__objects:
            serialized_objs[key] = __class__.__objects[key].to_dict()
        with open(__class__.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                dict_objs = json.load(file)
                for key, value in dict_objs.items():
                    cls_name = key.split('.')[0]
                    if cls_name in self.classes():
                        instance = self.classes()[cls_name](**value)
                        self.new(instance)
        except FileNotFoundError:
            pass
