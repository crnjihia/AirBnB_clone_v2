#!/usr/bin/python3
"""Test FileStorage Class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method"""
        self.storage.new(self.base_model)
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods"""
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, new_storage.all())

    def test_reload_nonexistent(self):
        """Test reload with nonexistent file"""
        try:
            os.remove("file.json")
        except:
            pass
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
