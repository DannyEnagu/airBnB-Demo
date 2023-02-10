#!/usr/bin/python3
"""Defines a ``base_model`` that contains the
    ``BaseModel`` class declaration
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Defines a new class ``BaseModel`` which is
       the parent class for classes like
       (User, State, City, Place…).

       Args:
        id (string): assign with an uuid when an instance is created
        created_at (datetime): assign with the current datetime
            when an instance is created
        updated_at (datatime): assign with the current datetime when
            an instance is created and it will be updated every time
            you change your object
    """
    def __init__(self, *args, **kwargs):
        """construct/initializes new instances of ``BaseModel``
           class.

        Args:
           id (string): assign with an uuid when an instance is
                       created.
           created_at (datetime): assign with the current datetime
                                  when an instance is created.
           updated_at (datatime): assign with the current datetime when
                                  an instance is created and it will be
                                  updated every time you change your object.
        """
        if kwargs and len(kwargs) > 0:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__setattr__(key, datetime.fromisoformat(kwargs[key]))
                    else:
                        self.__setattr__(key, kwargs[key])
        else:
            self.id = uuid4().__str__()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
           of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict

    def __str__(self):
        """Return the print() and str() representation of ``BaseModel``"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
