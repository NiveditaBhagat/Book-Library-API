from fastapi import FastAPI
from pydantic import BaseModel, Field,HTTPException
from typing import List

app = FastAPI()

# Pydantic model for a Book
class Book:
    id:int
    title: str =Field(min_length=3)
    author: str
    description: str
    rating : int
    year: int | None = Field(default=None)

    def __init__(self,id,title, author,description,rating,year):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.year=year

class Book_Request(BaseModel):
    

# Temporary in-memory "database"
books_db: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", year=1949),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
]



@app.get("/books",status_code=status.HTTP_200_OK)
def get_books():
    return books_db

@app.get("/books/{book_id}")  
def get_book(book_id:int):
    for book in books_db:
        if book.id==book_id:
            return book
        raise HTTPException(status_code=404, detail='Item not found')



@app.post("/books/")
def create_book(book: Book):    
    books_db.append(book)
    return {"message": "Book added successfully", "book": book}
    