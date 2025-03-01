#!/usr/bin/python3
"""Test module for the Amenity model."""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """Test class for the Amenity model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class for Amenity."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Checks the type of the name attribute."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
