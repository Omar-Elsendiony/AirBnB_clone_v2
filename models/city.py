#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import *


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    __tablename__ = 'cities'
    # id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    # state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state_id = mapped_column(ForeignKey("states.id"))
    # state: Mapped["State"] = relationship(backref="cities")
    place: Mapped["Place"] = relationship(backref="cities", cascade="all, delete-orphan")
