from pydantic import BaseModel

class Member(BaseModel):
    id: int
    name: str
    # Add other fields as needed

class MemberCreate(BaseModel):
    name: str
    # Add other fields as needed
from pydantic import BaseModel
from datetime import date
from typing import Optional

# ---------------- Members ----------------
class MemberBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    address: Optional[str]
    membership_date: date

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    member_id: int

    class Config:
        from_attributes = True

# ---------------- Books ----------------
class BookBase(BaseModel):
    title: str
    isbn: str
    published_year: Optional[int]
    copies_available: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int

    class Config:
        from_attributes = True
