#!/usr/bin/env python3
"""testcase for file_storage"""

import os
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import mock_open, patch


class TestFileStorage(unittest.TestCase):
    """this is testcase class for the the file storage"""
    def setUp(self):
        """this test is called before each test method run"""
        self.storage = FileStorage()

    def tearDown(self):
        """remove the files created by filestorage"""
        if os.path.exists(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)

    def test_all(self):
        """test the return of the empty dictionary"""
        self.assertEqual(self.storage.all, {})

    def test_new(self):
        """test id the new method add an object to __object"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_reload(self):
        """ Test if save and reload methods work together """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Save and reload
        self.storage.save()

        # Read the content of the JSON file
        with open(self.storage._FileStorage__file_path, 'r') as file_content:
            saved_data = json.load(file_content)

        # Assert that the saved data matches the expected structure
        key1 = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        key2 = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        self.assertIn(key1, saved_data)
        self.assertIn(key2, saved_data)

        # Assert that the loaded instances have the correct attributes
        loaded_obj1_data = saved_data[key1]
        loaded_obj2_data = saved_data[key2]
        loaded_obj1 = BaseModel(**loaded_obj1_data)
        loaded_obj2 = BaseModel(**loaded_obj2_data)
        self.assertEqual(loaded_obj1.to_dict(), obj1.to_dict())
        self.assertEqual(loaded_obj2.to_dict(), obj2.to_dict())

        new_storage = FileStorage()
        new_storage.reload()

        # Check if the instances are present in the reloaded storage
        self.assertIn(key1, new_storage.all())
        self.assertIn(key2, new_storage.all())
        self.assertEqual(new_storage.all()[key1].to_dict(), obj1.to_dict())
        self.assertEqual(new_storage.all()[key2].to_dict(), obj2.to_dict())


if __name__ == '__main__':
    unittest.main()
