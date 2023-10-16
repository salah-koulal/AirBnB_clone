#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
import pep8
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

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

    def test_instance_init_none(self):
        """Testing none"""
        instance = Place()
        instance.city_id = None
        instance.user_id = None
        instance.name = None
        instance.description = None
        instance.number_rooms = None
        instance.number_bathrooms = None
        instance.max_guest = None
        instance.price_by_night = None
        instance.latitude = None
        instance.longitude = None
        instance.amenity_ids = None
        self.assertEqual(instance.city_id, None)
        self.assertEqual(instance.user_id, None)
        self.assertEqual(instance.name, None)
        self.assertEqual(instance.description, None)
        self.assertEqual(instance.number_rooms, None)
        self.assertEqual(instance.number_bathrooms, None)
        self.assertEqual(instance.max_guest, None)
        self.assertEqual(instance.price_by_night, None)
        self.assertEqual(instance.latitude, None)
        self.assertEqual(instance.longitude, None)
        self.assertEqual(instance.amenity_ids, None)


if __name__ == '__main__':
    unittest.main()
