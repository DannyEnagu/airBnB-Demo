#!/usr/bin/python3
"""Defines a new model ``state`` that contains the
   ``State`` class.
"""
from .base_model import BaseModel


class State(BaseModel):
    """Defines a new class``State`` that inherits from ``BaseModel``

       Public attribute
         name: string - empty string
    """
    name = ""
