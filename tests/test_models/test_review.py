#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

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


if __name__ == '__main__':
    unittest.main()
