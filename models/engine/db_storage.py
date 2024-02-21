#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
#from models.base_model import BaseModel
import models
from models.base_model import Base
from models.state import State
from models import base_model


class DBStorage:
    """Database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Create a new instance of DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              '3306',  # Port remains unchanged
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects"""
        result = []
        if cls:
            cls_model = State
            query = self.__session.query(cls_model)
            for item in query:
                obj_info = "{}.{}".format(type(item).__name__, item.id)
                obj_dict = item.to_dict()
                result.append([type(item)] + [obj_info, obj_dict])
        else:
            classes = [
                getattr(
                    models,
                    name) for name in dir(models) if isinstance(
                    getattr(
                        models,
                        name),
                    type)]
            for c in classes:
                query = self.__session.query(c)
                for item in query:
                    obj_info = "{}.{}".format(type(item).__name__, item.id)
                    obj_dict = item.to_dict()
                    result.append([type(item)] + [obj_info, obj_dict])
        return result

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
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the current session"""
        self.__session.remove()
