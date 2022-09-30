#!/usr/bin/python3
"""Module for place, inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class, inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
