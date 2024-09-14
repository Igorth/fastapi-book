from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "Author 1",
        "category": 'math'
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Author 2",
        "category": 'fiction'
    },
    {
        "id": 3,
        "title": "Book 3",
        "author": "Author 3",
        "category": 'math'
    },
    {
        "id": 4,
        "title": "Book 4",
        "author": "Author 4",
        "category": 'history'
    },
    {
        "id": 5,
        "title": "Book 5",
        "author": "Author 4",
        "category": 'science'
    }
]


@app.get('/books')
async def get_all_books():
    return BOOKS


@app.get('/books/{book_title}')
async def get_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"detail": "Book not found"}


@app.get("/books/")
async def get_books_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/byauthor/")
async def get_all_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def get_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

