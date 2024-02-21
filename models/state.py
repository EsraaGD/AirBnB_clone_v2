#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base
from models.city import City


class State(BaseModel, Base):
    """ State class """

    # Add or replace these class attributes
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', cascade='all, delete-orphan', backref='state')

    # For FileStorage
    else:
        @property
        def cities(self):
            """ Getter attribute for cities in FileStorage """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
