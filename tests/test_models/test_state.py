#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_instance(self):
        """Testing a new created instance"""
        instance = State()
        instance.name = "State"
        self.assertEqual(State, type(instance))
        self.assertEqual(str, type(instance.id))
        self.assertEqual(instance.name, "State")
        expected_str = f"[State] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_init_none(self):
        """Testing none"""
        instance = State()
        instance.name = None
        self.assertEqual(instance.name, None)

if __name__ == "__main__":
    unittest.main()
