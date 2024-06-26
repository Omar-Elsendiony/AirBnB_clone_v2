#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from typing import Set
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    # id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities: Mapped[Set["City"]] = relationship(backref="state", cascade="all, delete-orphan")

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
