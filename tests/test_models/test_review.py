#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
import pep8
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

    cls = Review()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.cls)), res)

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.cls, Review)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.cls, 'place_id'))
        self.assertTrue(hasattr(self.cls, 'user_id'))
        self.assertTrue(hasattr(self.cls, 'text'))
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'created_at'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.cls.place_id, str)
        self.assertIsInstance(self.cls.user_id, str)
        self.assertIsInstance(self.cls.text, str)
        self.assertIsInstance(self.cls.id, str)
        self.assertIsInstance(self.cls.created_at, datetime.datetime)
        self.assertIsInstance(self.cls.updated_at, datetime.datetime)

    def test_instance_init_none(self):
        """Testing none"""
        instance = Review()
        instance.place_id = None
        instance.user_id = None
        instance.text = None
        self.assertEqual(instance.place_id, None)
        self.assertEqual(instance.user_id, None)
        self.assertEqual(instance.text, None)


if __name__ == '__main__':
    unittest.main()
