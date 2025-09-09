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
    id:Optional[int]=Field(description='Id is not needed to create', default=none)
    title:str=Field(min_length=3)
    author:str=Field(min_lenght=4)
    description:str=Field(min_length=4, maxmax_length=50)
    rating:int=Field(gt= -1,lt=6 )
    year:int=Field(gt=1999, lt=2031)

     model_config ={
        "json_schema_extra" : {
            "example" :{
                    "id":1
                 "title": "cse",
                 "author": "jcob",
                 "description": "cse book",
                 "rating": 3,
                 "year": 2012
            }
        }
    }
    

# Temporary in-memory "database"
books_db=[
    Book(1,'Comp Sceince','codingwithME','Nice book',4,2030),
    Book(2,'Fast API','author 2','api book',5,2030),
    Book(3,'Reacr','author 3','good book',4,2029),
    Book(4,'Comp network','author 4','network book',3, 2028),
    Book(5,'HP5','codingwithME','Hp book',2, 2027),
    Book(6,'HP6','codingwithME','readable book',1,2026)
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
def create_book(book_request: BookRequest):   
    print(type(BookRequest)) 
    new_book=Book(**book_request.model_dump())# converting the request to book object
    print(type(new_book))
    books_db.append(new_book)
    return {"message": "Book added successfully", "book": books_db}
    