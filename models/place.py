#!/usr/bin/python3
"""Defines a new model ``place`` that conttains the
   ``Place`` class.
"""
from .base_model import BaseModel


class Place(BaseModel):
    """Defines a new class``Place`` that inherits from ``BaseModel``

    Public Attributes:
       city_id: string - empty string: it will be the City.id
       user_id: string - empty string: it will be the User.id
       name: string - empty string
       description: string - empty string
       number_rooms: integer - 0
       number_bathrooms: integer - 0
       max_guest: integer - 0
       price_by_night: integer - 0
       latitude: float - 0.0
       longitude: float - 0.0
       amenity_ids: list of string - empty list: it will be the 
       list of Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longetitude = 0.0
    amenity_ids = []
