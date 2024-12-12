import pytest


@pytest.mark.asyncio
async def test_create_book(async_client):
    await async_client.post("/authors/", json={
        "first_name": "John",
        "last_name": "Smith",
        "birth_date": "1970-01-01"
    })
    response = await async_client.post("/books/", json={
        "title": "Book Title",
        "description": "A fascinating book.",
        "author_id": 1,
        "available_copies": 5
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Book Title"


@pytest.mark.asyncio
async def test_get_books(async_client):
    response = await async_client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_book_by_id(async_client):
    response = await async_client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_update_book(async_client):
    response = await async_client.put("/books/1", json={
        "title": "Updated Book Title",
        "description": "An updated description.",
        "author_id": 1,
        "available_copies": 3
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book Title"


@pytest.mark.asyncio
async def test_delete_book(async_client):
    response = await async_client.delete("/books/1")
    assert response.status_code == 200
    response = await async_client.get("/books/1")
    assert response.status_code == 404
