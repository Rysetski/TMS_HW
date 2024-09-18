from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    good_id = Column(Integer, ForeignKey("good.id"))
    address = Column(String)
    email = Column(String)
    notes = Column(String)

    good = relationship("Good", foreign_keys=[good_id])