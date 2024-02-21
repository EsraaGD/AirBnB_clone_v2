#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    # Add or replace these class attributes
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    # cities = relationship("City", back_populates="state",
    # cascade="all, delete-orphan")

    # For FileStorage
    # @property
    # def cities(self):
    #"""Getter attribute for cities"""
    #from models import storage
    # return [city for city in storage.all(City).values() if city.state_id ==
    # self.id]

    # For DB
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")

# For file storage
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
