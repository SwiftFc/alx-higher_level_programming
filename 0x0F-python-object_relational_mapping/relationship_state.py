#!/usr/bin/python3

"""
Module that contains the class definition of a State and an instance
Base = declarative_base():
Links to the MySQL table `states`
If the State object is deleted, all linked City objects
must be automatically deleted.
Also, the reference from a City object to his State should be named state.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Creating an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    Class representing the states table.
    Linked to MySQL table "states"
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
