from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "name": "Atomic Habits",
        "author": "James Clear",
        "published_year": 2018,
        "country": "United States",
        "language": "English",
        "price": 499
    },
    {
        "id": 2,
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "published_year": 1988,
        "country": "Brazil",
        "language": "Portuguese",
        "price": 399
    },
    {
        "id": 3,
        "name": "Clean Code",
        "author": "Robert C. Martin",
        "published_year": 2008,
        "country": "United States",
        "language": "English",
        "price": 699
    }
]

class Book(BaseModel):
    name:str
    author:str
    published_year:int
    country:str
    language:str
    price:int
    
def book_id():
    mx_id = 0
    for book in books:
        if book["id"]>mx_id:
            mx_id = book["id"]
    return mx_id+1

@app.get("/")
def home():
    return {"msg":"this api is a basic todo api"}

@app.get("/books")
def get_all_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@app.post("/books/create")
def add_book(book:Book):
    mx_id = book_id()
    new_book = {
        "id" : mx_id,
        **book.model_dump()
    }
    books.append(new_book)
    return {
        "message":"book appended successfully",
        "book" : new_book
    }

@app.put("/books/update/{book_id}")
def update_book(book_id:int,up_book:Book):
    c = False
    for book in books:
        if book["id"] == book_id:
            book["name"] = up_book.name
            book["author"] = up_book.author
            book["published_year"] = up_book.published_year
            book["country"] = up_book.country
            book["language"] = up_book.language
            book["price"] = up_book.price
            c = True
    if(c):
        return {
            "msg":"book updated successfull"
        }
    raise HTTPException(status_code=404,detail="book not found")
    

@app.patch("/books/delete/{book_id}")
def del_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"msg":"book deletion success"}
    raise HTTPException(status_code=404, detail="book not found")


