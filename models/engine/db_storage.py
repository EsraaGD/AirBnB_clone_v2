#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.base_model import Base
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Create a new instance of DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              '3306',  # Port remains unchanged
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Queries the current database session based on class name"""
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for class_ in classes:
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()
