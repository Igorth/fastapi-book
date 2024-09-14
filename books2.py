from fastapi import FastAPI, Body

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


BOOKS = [
    Book(1, 'Python', 'Likry', 'Very nice book', 5),
    Book(2, 'JavaScript', 'John Doe', 'Good book', 4),
    Book(3, 'Go', 'Jane Doe', 'Great book', 2),
    Book(4, 'Rust', 'David Johnson', 'Fantastic book', 4),
    Book(5, 'C#', 'Mary Smith', 'Excellent book', 3),
    Book(6, 'Java', 'John Williams', 'Average book', 3)
]


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
