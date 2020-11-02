from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    accounts = relationship("Account")

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    url = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
