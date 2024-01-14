#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ Representing the city class, contains state ID and name """
    state_id = ""
    name = ""
