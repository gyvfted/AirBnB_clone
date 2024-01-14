#!/usr/bin/python3
"""Place Test Documentation """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test cases """

    def __init__(self, *args, **kwargs):
        """Initialise tests """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Is ncity id a string """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Is new user id a string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Is name of place a string """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Is the description a string """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Is number of roome an integer """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Is number of bathrooms an integer """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Is max number of guests an integer """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Is night price an integer """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Are latitude coordinates float  """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Are longitutes coordinates float """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Are ids a list """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
