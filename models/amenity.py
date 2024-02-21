#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenities class is a subclass of BaseModel and Base"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
