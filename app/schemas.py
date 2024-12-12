from pydantic import BaseModel
from datetime import date


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    description: str | None = None
    author_id: int
    available_copies: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BorrowBase(BaseModel):
    book_id: int
    borrower_name: str
    borrow_date: date
    return_date: date | None = None


class BorrowCreate(BorrowBase):
    pass


class Borrow(BorrowBase):
    id: int

    class Config:
        orm_mode = True
