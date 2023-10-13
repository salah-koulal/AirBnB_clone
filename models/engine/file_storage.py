#!/usr/bin/python3

import json

class FileStorage:
    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key in __class__.__objects:
            serialized_objects[key] = __class__.__objects[key].to_dict()
        with open(__class__.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                from models.base_model import BaseModel
                dict_objs = json.load(file)
                for key in dict_objs:
                    if key.split(".")[0] == 'BaseModel':
                        __class__.__objects[key] = BaseModel(**dict_objs[key]) 
                                                    
        except FileNotFoundError:
            pass
