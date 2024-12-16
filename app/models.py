from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


# Модель для представления автора в базе данных
class Author(Base):
    # Указываем имя таблицы в базе данных
    tablename = "authors"
    # Идентификатор автора (первичный ключ)
    id = Column(Integer, primary_key=True, index=True)
    # Имя автора
    first_name = Column(String, nullable=False)
    # Фамилия автора
    last_name = Column(String, nullable=False)
    # Дата рождения автора
    birth_date = Column(Date, nullable=False)
    # Связь "один ко многим" с книгами
    books = relationship("Book", back_populates="author")


# Модель для представления книги в базе данных
class Book(Base):
    # Указываем имя таблицы в базе данных
    tablename = "books"
    # Идентификатор книги (первичный ключ)
    id = Column(Integer, primary_key=True, index=True)
    # Название книги
    title = Column(String, nullable=False)
    # Описание книги (может быть пустым)
    description = Column(Text, nullable=True)
    # Идентификатор автора (внешний ключ)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    # Количество доступных экземпляров книги
    available_copies = Column(Integer, nullable=False, default=1)
    # Связь "многие к одному" с автором
    author = relationship("Author", back_populates="books")


# Модель для представления записи о взятии книги в базе данных
class Borrow(Base):
    # Указываем имя таблицы в базе данных
    tablename = "borrows"
    # Идентификатор записи (первичный ключ)
    id = Column(Integer, primary_key=True, index=True)
    # Идентификатор книги (внешний ключ)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    # Имя заемщика
    borrower_name = Column(String, nullable=False)
    # Дата взятия книги
    borrow_date = Column(Date, nullable=False)
    # Дата возврата книги (может быть пустой)
    return_date = Column(Date, nullable=True)
    # Связь "многие к одному" с книгой
    book = relationship("Book")
