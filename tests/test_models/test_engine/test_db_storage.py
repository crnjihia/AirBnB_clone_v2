#!/usr/bin/python3
"""Test DBStorage Class"""
import unittest
import os
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage class"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                    "DB Storage not in use")
    def setUp(self):
        """Set up test cases"""
        self.storage = DBStorage()
        self.storage.reload()

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_save(self):
        """Test new and save methods"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        key = f"State.{state.id}"
        self.assertIn(key, self.storage.all())

    def test_delete(self):
        """Test delete method"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        key = f"State.{state.id}"
        self.assertNotIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
