#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    cls = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.cls)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.cls, Place)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.cls, 'city_id'))
        self.assertTrue(hasattr(self.cls, 'user_id'))
        self.assertTrue(hasattr(self.cls, 'name'))
        self.assertTrue(hasattr(self.cls, 'description'))
        self.assertTrue(hasattr(self.cls, 'number_rooms'))
        self.assertTrue(hasattr(self.cls, 'number_bathrooms'))
        self.assertTrue(hasattr(self.cls, 'max_guest'))
        self.assertTrue(hasattr(self.cls, 'price_by_night'))
        self.assertTrue(hasattr(self.cls, 'latitude'))
        self.assertTrue(hasattr(self.cls, 'longitude'))
        self.assertTrue(hasattr(self.cls, 'amenity_ids'))
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'created_at'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.cls.city_id, str)
        self.assertIsInstance(self.cls.user_id, str)
        self.assertIsInstance(self.cls.name, str)
        self.assertIsInstance(self.cls.description, str)
        self.assertIsInstance(self.cls.number_rooms, int)
        self.assertIsInstance(self.cls.number_bathrooms, int)
        self.assertIsInstance(self.cls.max_guest, int)
        self.assertIsInstance(self.cls.price_by_night, int)
        self.assertIsInstance(self.cls.latitude, float)
        self.assertIsInstance(self.cls.longitude, float)
        self.assertIsInstance(self.cls.amenity_ids, list)
        self.assertIsInstance(self.cls.id, str)
        self.assertIsInstance(self.cls.created_at, datetime.datetime)
        self.assertIsInstance(self.cls.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
