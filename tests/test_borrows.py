import pytest
from datetime import date  # Импортируем класс date для работы с датами


@pytest.mark.asyncio
async def test_create_borrow(async_client):
    """
    Тест для проверки создания записи о выдаче книги (borrow).
    """
    # Сначала создаем автора
    await async_client.post("/authors/", json={
        "first_name": "Jane",
        "last_name": "Austen",
        "birth_date": "1775-12-16"
    })
    # Затем создаем книгу
    await async_client.post("/books/", json={
        "title": "Pride and Prejudice",
        "description": "A classic novel.",
        "author_id": 1,
        "available_copies": 2
    })
    # Теперь создаем запись о выдаче книги
    response = await async_client.post("/borrows/", json={
        "book_id": 1,  # Указываем ID книги
        "borrower_name": "Alice",  # Указываем имя заёмщика
        "borrow_date": str(date.today())  # Указываем текущую дату выдачи
    })
    assert response.status_code == 200  # Проверяем, что запрос успешен
    assert response.json()[
               "borrower_name"] == "Alice"  # Проверяем, что имя заёмщика в ответе соответствует отправленному


@pytest.mark.asyncio
async def test_get_borrows(async_client):
    """
    Тест для проверки получения списка всех записей о выдаче книг.
    """
    response = await async_client.get("/borrows/")  # Запрашиваем список всех выдач
    assert response.status_code == 200  # Проверяем, что запрос успешен
    assert len(response.json()) > 0  # Проверяем, что список не пуст. Предполагается наличие хотя бы одной записи


@pytest.mark.asyncio
async def test_get_borrow_by_id(async_client):
    """
    Тест для проверки получения записи о выдаче книги по её ID.
    """
    response = await async_client.get("/borrows/1")  # Запрашиваем запись о выдаче по id 1
    assert response.status_code == 200  # Проверяем, что запрос успешен
    assert response.json()[
               "id"] == 1  # Проверяем, что ID записи в ответе соответствует запрошенному. Предполагается, что запись с id 1 существует.


@pytest.mark.asyncio
async def test_return_borrow(async_client):
    """
    Тест для проверки обновления записи о возврате книги.
    """
    response = await async_client.patch("/borrows/1/return",
                                        json={  # Выполняем PATCH-запрос на эндпоинт для возврата, с указанием ID выдачи
                                            "return_date": str(date.today())  # Указываем текущую дату возврата
                                        })
    assert response.status_code == 200  # Проверяем, что запрос успешен
    assert response.json()["return_date"] == str(
        date.today())  # Проверяем, что дата возврата в ответе соответствует текущей дате
