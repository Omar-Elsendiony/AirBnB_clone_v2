#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
