#!/usr/bin/python3
"""Test module for the City model."""
import os

from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestCity(TestBasemodel):
    """Test class for the City model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class for City."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Checks the type of the state_id attribute."""
        new = self.value()
        self.assertEqual(
            type(new.state_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """Checks the type of the name attribute."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
