from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Member(Base):
    __tablename__ = "Members"

    member_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), unique=True)
    address = Column(String(200))
    membership_date = Column(Date, nullable=False)

class Book(Base):
    __tablename__ = "Books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    published_year = Column(Integer)
    copies_available = Column(Integer, nullable=False)
