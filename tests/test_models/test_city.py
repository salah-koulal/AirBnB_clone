#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.city import City
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    cls = City()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.cls)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.cls, City)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.cls, 'state_id'))
        self.assertTrue(hasattr(self.cls, 'name'))
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'created_at'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.cls.state_id, str)
        self.assertIsInstance(self.cls.name, str)
        self.assertIsInstance(self.cls.id, str)
        self.assertIsInstance(self.cls.created_at, datetime.datetime)
        self.assertIsInstance(self.cls.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
