#!/usr/bin/python3
"""State test Documentation """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    ""Test cases to go through" """

    def __init__(self, *args, **kwargs):
        """Initialise tests """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Is name of state a string """
        new = self.value()
        self.assertEqual(type(new.name), str)
