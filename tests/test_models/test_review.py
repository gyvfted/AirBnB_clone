#!/usr/bin/python3
"""Review test documentation """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Review test cases """

    def __init__(self, *args, **kwargs):
        """Initialise the tests """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Is the place id a strind """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Is the user id a string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Is the actual review a string """
        new = self.value()
        self.assertEqual(type(new.text), str)
