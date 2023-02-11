#!/usr/bin/python3
"""Defines the model ``file_storage`` that
   contains ``FileStorage`` class
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import os.path

cls = {
        "Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User
      }


class FileStorage:
    """The ``FileStorage`` class serializes instances
       to a JSON file and deserializes JSON file to instances

    Attributes:
       __file_path (string): path to the JSON file (ex: file.json)
       __objects (dictionary): stores objects by id (ex: BaseModel.12121212)
    """
    __file_Path = "./file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary that contains all object"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
             obj (object): new object to add to __object
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        filename = self.__file_Path
        with open(filename, "w") as jsonfile:
            tmp_objs = {}
            for key in self.__objects:
                tmp_objs[key] = self.__objects[key].to_dict()
            json.dump(tmp_objs, jsonfile, indent=4)

    def reload(self):
        filename = self.__file_Path
        if os.path.exists(filename):
            with open(filename, "r") as jsonfile:
                ds = json.load(jsonfile)
                for k in ds:
                    self.__objects[k] = cls[ds[k]["__class__"]](**ds[k])
