#!/usr/bin/python3
"""Module defining the Review class for the HBNB project."""
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Class to store review details."""
    __tablename__ = 'reviews'
    place_id = Column(
        String(60), ForeignKey('places.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
