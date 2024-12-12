import pytest


@pytest.mark.asyncio
async def test_create_author(async_client):
    response = await async_client.post("/authors/", json={
        "first_name": "John",
        "last_name": "Doe",
        "birth_date": "1980-01-01"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "John"


@pytest.mark.asyncio
async def test_get_authors(async_client):
    response = await async_client.get("/authors/")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_author_by_id(async_client):
    response = await async_client.get("/authors/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_update_author(async_client):
    response = await async_client.put("/authors/1", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "birth_date": "1980-01-01"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Jane"


@pytest.mark.asyncio
async def test_delete_author(async_client):
    response = await async_client.delete("/authors/1")
    assert response.status_code == 200
    response = await async_client.get("/authors/1")
    assert response.status_code == 404
