import pytest
from datetime import date


@pytest.mark.asyncio
async def test_create_borrow(async_client):
    await async_client.post("/authors/", json={
        "first_name": "Jane",
        "last_name": "Austen",
        "birth_date": "1775-12-16"
    })
    await async_client.post("/books/", json={
        "title": "Pride and Prejudice",
        "description": "A classic novel.",
        "author_id": 1,
        "available_copies": 2
    })
    response = await async_client.post("/borrows/", json={
        "book_id": 1,
        "borrower_name": "Alice",
        "borrow_date": str(date.today())
    })
    assert response.status_code == 200
    assert response.json()["borrower_name"] == "Alice"


@pytest.mark.asyncio
async def test_get_borrows(async_client):
    response = await async_client.get("/borrows/")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_borrow_by_id(async_client):
    response = await async_client.get("/borrows/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_return_borrow(async_client):
    response = await async_client.patch("/borrows/1/return", json={
        "return_date": str(date.today())
    })
    assert response.status_code == 200
    assert response.json()["return_date"] == str(date.today())
