#!/usr/bin/python3
"""Defines the model ``file_storage`` that
   contains ``FileStorage`` class
"""
import json
import os.path


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
        #print(obj.id)
        #print(obj.to_dict())
        #print(obj.__class__.__name__)
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()
#        print(self.__objects)
#        print("______-OK___________")

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        filename = self.__file_Path
        with open(filename, "w") as jsonfile:
#            print(type(self.__objects["updated_at"]))
            json.dump(self.__objects, jsonfile, indent=4)

    def reload(self):
        filename = self.__file_Path
        if os.path.exists(filename):
                with open(filename, "r") as jsonfile:
                    self.__objects = json.load(jsonfile)
                    #FileStorage.__objects = {self.new(obj) for obj in py_dict}
