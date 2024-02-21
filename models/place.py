#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review", cascade="all, delete-orphan", backref="place")

    else:
        @property
        def reviews(self):
            """ Getter attribute for reviews in FileStorage """
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity", secondary="place_amenities",
                                 back_populates="place_amenities")
    else:
        @property
        def amenities(self):
            """ Getter attribute for amenities in FileStorage """
            from models import storage
            amenity_list = []
            for amenity_id in self.amenity_id:
                amenity = storage.get("Amenity", amenity_id)
                if amenity:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            """ Setter method to add an Amenity to Place object """
            if isinstance(amenity, Amenity):
                self.amenity_id.append(amenity.id)
