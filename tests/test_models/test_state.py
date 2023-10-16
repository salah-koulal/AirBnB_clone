#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
import pep8
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

    def test_instance(self):
        """Testing a new created instance"""
        instance = State()
        instance.name = "State"
        self.assertEqual(State, type(instance))
        self.assertEqual(str, type(instance.id))
        self.assertEqual(instance.name, "State")
        self.assertEqual(datetime, type(instance.created_at))
        expected_str = f"[State] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_id_unique(self):
        "testing"
        instance_1 = State()
        instance_2 = State()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_init_none(self):
        """Testing none"""
        instance = State()
        instance.name = None
        self.assertEqual(instance.name, None)


if __name__ == "__main__":
    unittest.main()
