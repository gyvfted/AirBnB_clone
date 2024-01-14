#!/usr/bin/python3
"""Test for Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test cases for Amenity """

    def __init__(self, *args, **kwargs):
        """Is Amenoty empty """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Is Amenity a string data type """
        new = self.value()
        self.assertEqual(type(new.name), str)
