from database import Base
from sqlalchemy import Column, Integer, String, Float

class Transaction(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    ingredients = Column(String)
    directions = Column(String)