#!/usr/bin/python3
"""City Test Documentation """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """City test cases """

    def __init__(self, *args, **kwargs):
        """Is City name City """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Is state id a string """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Is name a string datatype """
        new = self.value()
        self.assertEqual(type(new.name), str)
