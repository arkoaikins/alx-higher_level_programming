#!/usr/bin/python3
"""
This script contains the class definition of a City
"""
from model_state import Base,State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    Class that defines each city
    att:
    __tablename__:table name of the class
    id:The city id of the class
    name:The city name of the class
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
