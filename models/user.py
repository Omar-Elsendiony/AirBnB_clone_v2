#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import *


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    # id = Column(String(60), primary_key=True, nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
