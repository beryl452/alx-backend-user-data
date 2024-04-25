#!/usr/bin/env python3
"""User model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """Represents a record from the `users` table.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, Nullable=False)
    hashed_password = Column(string, Nullable=True)
    session_id = Column(string, Nullable=True)
    reset_token = Column(string, Nullable=True)
