from pydantic import BaseModel
from datetime import date


# Базовая схема для представления автора
class AuthorBase(BaseModel):
    # Имя автора
    first_name: str
    # Фамилия автора
    last_name: str
    # Дата рождения автора
    birth_date: date


# Схема для создания нового автора (наследуется от базовой)
class AuthorCreate(AuthorBase):
    pass


# Схема для отображения автора (с дополнительным полем id)
class Author(AuthorBase):
    # Идентификатор автора
    id: int

    # Настройка для поддержки работы с ORM
    class Config:
        orm_mode = True


# Базовая схема для представления книги
class BookBase(BaseModel):
    # Название книги
    title: str
    # Описание книги (опционально)
    description: str | None = None
    # Идентификатор автора книги
    author_id: int
    # Количество доступных экземпляров книги
    available_copies: int


# Схема для создания новой книги (наследуется от базовой)
class BookCreate(BookBase):
    pass


# Схема для отображения книги (с дополнительным полем id)
class Book(BookBase):
    # Идентификатор книги
    id: int

    # Настройка для поддержки работы с ORM
    class Config:
        orm_mode = True


# Базовая схема для представления записи о взятии книги
class BorrowBase(BaseModel):
    # Идентификатор книги
    book_id: int
    # Имя заемщика
    borrower_name: str
    # Дата взятия книги
    borrow_date: date
    # Дата возврата книги (опционально)
    return_date: date | None = None


# Схема для создания новой записи о взятии книги (наследуется от базовой)
class BorrowCreate(BorrowBase):
    pass


# Схема для отображения записи о взятии книги (с дополнительным полем id)
class Borrow(BorrowBase):
    # Идентификатор записи
    id: int

    # Настройка для поддержки работы с ORM
    class Config:
        orm_mode = True
