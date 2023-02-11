#!/usr/bin/python3
"""Defines a new model ``user`` that conttains the
   ``User`` class.
"""
from .base_model import BaseModel


class User(BaseModel):
    """Defines a new class``User`` that inherits from ``BaseModel``

    Public Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
