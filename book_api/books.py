from book_api.database import books
from book_api.models import Book
from fastapi import APIRouter,HTTPException,status
from book_api.models import BookResponse
from typing import List
router = APIRouter()

def book_id():
    mx_id = 0
    for book in books:
        if book["id"]>mx_id:
            mx_id = book["id"]
    return mx_id+1

@router.get("/")
def home():
    return {"msg":"this api is a basic todo api"}

@router.get("/books",response_model=List[BookResponse],status_code=status.HTTP_200_OK)
def get_all_books():
    return books

@router.get("/books/{book_id}",status_code=status.HTTP_200_OK)
def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@router.post("/books",status_code=status.HTTP_201_CREATED)
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

@router.put("/books/{book_id}",status_code=status.HTTP_200_OK)
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
    

@router.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def del_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"msg":"book deletion success"}
    raise HTTPException(status_code=404, detail="book not found")
