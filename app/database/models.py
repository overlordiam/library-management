from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, nullable=True)
    publication_year = Column(Integer, nullable=True)
    genre = Column(String, nullable=True)
    is_available = Column(Boolean, default=True)
    borrower_name = Column(String, nullable=True)
    checkout_date = Column(DateTime, nullable=True)
    return_date = Column(DateTime, nullable=True) 