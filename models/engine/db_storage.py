#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """ Database storage class """

    # Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the database storage """
        # Retrieve environment variables
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        # Create the engine
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(user, password, host, database),
            pool_pre_ping=True
        )

        # Drop all tables if HBNB_ENV is equal to test
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create tables if not exists
        Base.metadata.create_all(self.__engine)

        # Create a scoped session
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )

    def all(self, cls=None):
        """ Queries on the current database session """
        from models import classes

        if cls:
            return self.__session.query(classes[cls]).all()
        else:
            return self.__session.query(
                classes['User'], classes['State'],
                classes['City'], classes['Amenity'],
                classes['Place'], classes['Review']
            ).all()

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the object from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and creates the current
        database session """
        from models import classes
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes the current database session """
        self.__session.remove()
