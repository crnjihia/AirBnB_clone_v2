#!/usr/bin/python3
"""This module creates an instance of the storage engine."""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""Singleton instance of the storage engine for model management.
"""
storage.reload()
