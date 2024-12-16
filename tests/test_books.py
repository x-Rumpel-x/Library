import pytest


@pytest.mark.asyncio
async def test_create_book(async_client):
    """
    Тест создания книги.
    """
    # Сначала необходимо создать автора, чтобы книга могла быть связана с ним
    await async_client.post("/authors/", json={
        "first_name": "John",
        "last_name": "Smith",
        "birth_date": "1970-01-01"
    })
    # Теперь создаем книгу
    response = await async_client.post("/books/", json={
        "title": "Book Title",
        "description": "A fascinating book.",
        "author_id": 1,  # Предполагается, что автор с id 1 уже существует
        "available_copies": 5
    })
    assert response.status_code == 200  # Проверка статуса ответа
    assert response.json()["title"] == "Book Title"  # Проверка, что созданная книга имеет правильное название


@pytest.mark.asyncio
async def test_get_books(async_client):
    """
    Тест получения списка книг.
    """
    response = await async_client.get("/books/")  # Запрос на получение списка книг
    assert response.status_code == 200  # Проверка статуса ответа
    assert len(response.json()) > 0  # Проверка, что список не пуст.  Предполагается, что хотя бы одна книга существует


@pytest.mark.asyncio
async def test_get_book_by_id(async_client):
    """
    Тест получения книги по идентификатору.
    """
    response = await async_client.get("/books/1")  # Запрос на получение книги по id 1
    assert response.status_code == 200  # Проверка статуса ответа
    assert response.json()[
               "id"] == 1  # Проверка, что полученная книга имеет правильный идентификатор.  Предполагается, что книга с id 1 существует.


@pytest.mark.asyncio
async def test_update_book(async_client):
    """
    Тест обновления книги.
    """
    response = await async_client.put("/books/1", json={
        "title": "Updated Book Title",
        "description": "An updated description.",
        "author_id": 1,
        "available_copies": 3
    })
    assert response.status_code == 200  # Проверка статуса ответа
    assert response.json()["title"] == "Updated Book Title"  # Проверка, что книга обновлена с правильным названием


@pytest.mark.asyncio
async def test_delete_book(async_client):
    """
    Тест удаления книги.
    """
    response = await async_client.delete("/books/1")  # Удаление книги
    assert response.status_code == 200  # Проверка статуса ответа при удалении
    response = await async_client.get("/books/1")  # Проверка, что книги нет
    assert response.status_code == 404  # Проверка статуса ответа при попытке получить несуществующую книгу
