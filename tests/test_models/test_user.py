#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
import pep8
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

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
