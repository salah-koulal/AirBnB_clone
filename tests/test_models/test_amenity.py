#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    cls = Amenity()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.cls)), res)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.cls, Amenity)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.cls, 'name'))
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'created_at'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.cls.name, str)
        self.assertIsInstance(self.cls.id, str)
        self.assertIsInstance(self.cls.created_at, datetime.datetime)
        self.assertIsInstance(self.cls.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
