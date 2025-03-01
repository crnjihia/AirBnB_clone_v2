#!/usr/bin/python3
"""Test module for the State model."""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """Test class for the State model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class for State."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Checks the type of the name attribute."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
