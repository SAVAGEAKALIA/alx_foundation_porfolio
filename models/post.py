#!/usr/bin/env python

import os
# from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    __tablename__ = "posts"
    title = Column(String(128), nullable=False)
    body = Column(String(5000), nullable=False)
    # author = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    def format_for_display(self):
        """Format the post for display"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.body[:5000] + '...' if len(self.body) > 5000 else self.body,
            # 'author': self.author or 'Anonymous',
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }