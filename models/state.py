#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    # Add or replace these class attributes
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute for cities"""
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
