from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library CRUD API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- Member Routes ----------------
@app.get("/members", response_model=list[schemas.Member])
def read_members(db: Session = Depends(get_db)):
    return crud.get_members(db)

@app.post("/members", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db, member)

@app.put("/members/{member_id}", response_model=schemas.Member)
def update_member(member_id: int, member: schemas.MemberCreate, db: Session = Depends(get_db)):
    db_member = crud.update_member(db, member_id, member)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.delete("/members/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.delete_member(db, member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member deleted"}

# ---------------- Book Routes ----------------
@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
