#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from dotenv import load_dotenv
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()

# Load environment variables from .env file
load_dotenv()


class BaseModel:
    """
    Base Model class that will be the parent of all other classes.
    It includes common attributes and methods.
    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class.
        If the id is not provided, generate a random UUID.
        If the created_at and updated_at attributes are not provided,
        set them to the current time.
        """
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.utcnow()

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.save()

    def save(self):
        """
        Save the current state of the object into the database.
        """
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """
        Return a string representation of the BaseModel class.
        """
        # f"BlogPost('{self.title}', '{self.date_created}')"
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel class.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.strftime(time)
        return dictionary

    def delete(self):
        """
        Delete the current object from the database.
        """
        models.storage.delete(self)
