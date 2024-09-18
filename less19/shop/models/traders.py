from sqlalchemy import Column, Integer, String

from .base import Base

class Trader(Base):
    __tablename__ = "trader"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String)
    lastname = Column(String)
    email = Column(String)
    address = Column(String)

    def __repr__(self):
        pass
