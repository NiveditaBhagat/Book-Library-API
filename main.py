from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Pydantic model for a Book
class Book(BaseModel):
    id:int
    title: str
    author: str
    year: int | None = Field(default=None)


# Temporary in-memory "database"
books_db: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", year=1949),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
]



@app.get("/books")
def get_books():
    return books_db

@app.get("/books/{book_id}")  
def get_book(book_id:int):
    for book in books_db:
        if book.id==book_id:
            return book



@app.post("/books/")
def create_book(book: Book):    
    books_db.append(book)
    return {"message": "Book added successfully", "book": book}
    