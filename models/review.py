#!/usr/bin/python3
"""Defines a new model ``review`` that conttains the
   ``Review`` class.
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Defines a new class``Review`` that inherits from ``BaseModel``

    Public Attributes:
       place_id: string - empty string: it will be the Place.id
       user_id: string - empty string: it will be the User.id
       text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
