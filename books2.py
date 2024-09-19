from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "John author",
                "description": "A new book description",
                "rating": 5
            }
        }
    }


BOOKS = [
    Book(1, 'Python', 'Jack Jan', 'Very nice book', 5),
    Book(2, 'JavaScript', 'John Doe', 'Good book', 4),
    Book(3, 'Go', 'Jane Doe', 'Great book', 2),
    Book(4, 'Rust', 'David Johnson', 'Fantastic book', 4),
    Book(5, 'C#', 'Mary Smith', 'Excellent book', 3),
    Book(6, 'Java', 'John Williams', 'Average book', 3)
]


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book")
async def create_book(book_request: BookRequest):  # book_request is a type of BookRequest
    new_book = Book(**book_request.model_dump())  # converting the request to Book object
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book
