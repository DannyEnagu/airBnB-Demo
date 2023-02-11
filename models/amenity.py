#!/usr/bin/python3
"""Defines a new model ``amenity`` that conttains the
   ``Amenity`` class.
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Defines a new class``Amenity`` that inherits from ``BaseModel``

     Public Attributes:
        name: string - empty string
    """
    name = ""
