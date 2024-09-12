#!/usr/bin/env python

import models
from models.post import Post
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Post": Post}


class DBStorage:
    """interacts with the MySQL database"""
    __session = None
    __engine = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        # self.__engine = create_engine(getenv('HBNB_MYSQL_URI'), pool_pre_ping=True)
        # Base.metadata.create_all(self.__engine)
        # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        # self.__session = scoped_session(SessionLocal)
        blog_user = getenv("BLOG_USER")
        blog_pwd = getenv("BLOG_PWD")
        blog_host = getenv("BLOG_HOST")
        blog_db = getenv("BLOG_DB")
        db_base = f"mysql+mysqldb://{blog_user}:{blog_pwd}@{blog_host}/{blog_db}"

        if not all(db_base):
            raise ValueError("Missing MySQL URI")

        self.__engine = create_engine(db_base, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

    def all(self, cls):
        """Query class and return all"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def commit(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def close(self):
        """call remove() on the private session attribute"""
        self.__session.remove()

    def delete(self, obj):
        """Delete object from the database"""
        self.__session.delete(obj)

    # def __repr__(self):
    #     """return a string representation of the class"""
    #     # f"BlogPost('{self.title}', '{self.date_created}')"
    #     # return "<DBStorage {}>".format(self.__class__.__name__)
    #     return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
    #                                  self.__dict__)

    def reload(self):
        """reloads the state of the session from the database"""
        Base.metadata.create_all(self.__engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.__session = scoped_session(SessionLocal)

    # def get_session(self, cls, id):
    #     """Return the current session"""
    #     if cls not in classes.values():
    #         return None
    #     key = cls.__name__ + '.' + id
    #     if key in self.__session.query(cls).all():
    #         return self.__session.query(cls).filter_by(id=id).first()
    #     return None

    def get(self, cls, id):
        """Return the object with class cls and id from the database"""

        if cls not in classes.values():
            return f'{cls} not in {classes.values()}'
        key = cls.__name__ + '.' + id
        # print(f'key: {key}')
        # print(f'{self.__session.query(cls).all()}')
        all_objects = self.all(cls)
        # print(f'All objects: {all_objects}')
        if key in all_objects:
            return all_objects[key]
        return None
        # if key in self.__session.query(cls).all():
        #     return self.__session.query(cls).filter_by(id=id).first()
        # return None
