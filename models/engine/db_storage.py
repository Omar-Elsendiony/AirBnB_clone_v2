#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine =  None
    __session = None

    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }
    
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        # else:
        #     Base.metadata.create_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objectsToReturn = {}
        classNames = ['User', 'Place', 'State', 'City', 'Amenity', 'Review']
        if (cls is not None):
            allObjectsSingleClass = self.__session.query(self.classes[cls]).all() # returns all objects of one class
            for object in allObjectsSingleClass:
                key = object.__class__.__name__ + '.' + object.id
                objectsToReturn.update({key: object})
        else:
            for className in classNames:
                allObjectsSingleClass = self.__session.query(self.classes[className]).all()
                for object in allObjectsSingleClass:
                    key = object.__class__.__name__ + '.' + object.id
                    objectsToReturn.update({key: object})
        return objectsToReturn
    
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        # Base.metadata.create_all(self.__engine)
        self.__session.commit()
       
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
        
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
