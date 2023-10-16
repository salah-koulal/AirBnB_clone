#!/usr/bin/python3
"""
This module tests the base class
"""
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def test_pep8_compliance(self):
        """ Test PEP8 compliance using pycodestyle"""
        pycodestyle = pep8.StyleGuide(quiet=True)
        file_paths = ["models/user.py"]
        result = pycodestyle.check_files(file_paths)
        error_message = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error_message)

    def test_init(self):
        """Test if id, created_at, and updated_at exists and their types.
        """
        my_model = BaseModel()
        self.assertTrue(type(my_model.id), str)
        self.assertTrue(len(my_model.id), 36)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)
        self.assertEqual(my_model.updated_at, my_model.created_at)

    def test_instance(self):
        """Testing a new created instance"""
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertEqual(BaseModel, type(instance_1))
        self.assertEqual(str, type(instance_1.id))
        self.assertEqual(datetime, type(instance_1.created_at))
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_updated_time(self):
        """check if updated time is changed when new attrbutes created and the
        save function is called.
        """
        my_model = BaseModel()
        my_model.name = "Alx School"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(my_model.updated_at, my_model.created_at)

    def test_str_representaion(self):
        """string representaion test.
        """
        my_model = BaseModel()
        my_model.name = "Alx School"
        my_model.my_number = 89
        self.assertEqual(str(my_model),
                         '[{}] ({}) {}'.format(my_model.__class__.__name__,
                                               my_model.id,
                                               my_model.__dict__))

    def test_instance_created_at(self):
        "testing"
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))

    def test_kwargs(self):
        """Test basemodel is created correctly from dictionay.
        """
        my_model = BaseModel()
        my_model.name = "Alx School"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(str(my_model), str(my_new_model))
        self.assertFalse(my_model is my_new_model)

    def test_kwargs(self):
        my_model = BaseModel()
        my_model.name = "Alx School"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(str(my_model), str(my_new_model))
        self.assertFalse(my_model is my_new_model)

    def test_object_to_dict(self):
        """Testing To_dict method"""
        instance = BaseModel()
        instance.name = "Alx School"
        instance.my_number = 89
        dictionary = instance.to_dict()
        dictionary_cmp = {
            'my_number': 89,
            'name': 'Alx School',
            '__class__': 'BaseModel',
            'updated_at': instance.updated_at.isoformat(),
            'id': instance.id,
            'created_at': instance.created_at.isoformat()
        }

        # Define a tolerance for timestamp comparison (e.g., 1 second)
        timestamp_tolerance = timedelta(seconds=1)


if __name__ == '__main__':
    unittest.main()
