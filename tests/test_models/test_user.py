#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def test_instance_none(self):
        """Testing none"""
        new_user = User()
        new_user.email = None
        new_user.password = None
        new_user.first_name = None
        new_user.last_name = None
        self.assertEqual(new_user.email, None)
        self.assertEqual(new_user.password, None)
        self.assertEqual(new_user.first_name, None)
        self.assertEqual(new_user.last_name, None)

if __name__ == "__main__":
    unittest.main()
