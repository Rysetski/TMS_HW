from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Good(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String) 
    category_id = Column(Integer, ForeignKey("category.id"))
    trader_id = Column(Integer, ForeignKey("trader.id"))

    category = relationship("Category", foreign_keys=[category_id])
    trader = relationship("Trader", foreign_keys=[trader_id])

    def __repr__(self):
        return f"Good(id={self.id}, name={self.name}, category={self.category.name}, trader={self.trader.firstName})"