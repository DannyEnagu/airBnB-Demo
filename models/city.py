#!/usr/bin/python3
"""Defines a new model ``city`` that conttains the
   ``City`` class.
"""
from .base_model import BaseModel

class City(BaseModel):
    """Defines a new class``City`` that inherits from ``BaseModel``

    Public Attributes
       state_id: string - empty string: it will be the State.id
       name: string - empty string
    """
    state_id = ""
    name = ""
