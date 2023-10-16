#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
import pep8
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

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

    def test_instance_created_at(self):
        "testing"
        instance = Amenity()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_none(self):
        """Testing none"""
        instance = Amenity()
        instance.name = None
        self.assertEqual(instance.name, None)


if __name__ == '__main__':
    unittest.main()
