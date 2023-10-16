#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
import pep8
from models.city import City
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

    def test_instance_id_unique(self):
        "testing"
        instance_1 = City()
        instance_2 = City()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        "testing"
        instance = City()
        expected_str = f"[City] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        "testing"
        instance = City()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = City()
        instance.name = "Monaco"
        self.assertEqual(instance.name, "Monaco")

    def test_instance_init_none(self):
        """Testing none"""
        instance = City()
        instance.state_id = None
        instance.name = None
        self.assertEqual(instance.state_id, None)
        self.assertEqual(instance.name, None)


if __name__ == '__main__':
    unittest.main()
