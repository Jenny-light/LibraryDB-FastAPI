from sqlalchemy.orm import Session
from . import models, schemas

# ---------------- Members ----------------
def get_members(db: Session):
    return db.query(models.Member).all()

def create_member(db: Session, member: schemas.MemberCreate):
    new_member = models.Member(**member.dict())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

def update_member(db: Session, member_id: int, member: schemas.MemberCreate):
    db_member = db.query(models.Member).filter(models.Member.member_id == member_id).first()
    if db_member:
        for key, value in member.dict().items():
            setattr(db_member, key, value)
        db.commit()
        db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: int):
    db_member = db.query(models.Member).filter(models.Member.member_id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
    return db_member

# ---------------- Books ----------------
def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    if db_book:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
