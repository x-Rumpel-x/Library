import pytest  # Импортируем библиотеку pytest для тестирования


@pytest.mark.asyncio  # Маркируем тест как асинхронный
async def test_create_author(async_client):
    """
    Тест для проверки создания автора.
    """
    response = await async_client.post("/authors/",
                                       json={  # Выполняем POST-запрос на эндпоинт "/authors/" с JSON-данными
                                           "first_name": "John",
                                           "last_name": "Doe",
                                           "birth_date": "1980-01-01"
                                       })
    assert response.status_code == 200  # Проверяем, что статус-код ответа равен 200 (OK)
    assert response.json()["first_name"] == "John"  # Проверяем, что имя автора в ответе соответствует отправленному


@pytest.mark.asyncio  # Маркируем тест как асинхронный
async def test_get_authors(async_client):
    """
    Тест для проверки получения списка авторов.
    """
    response = await async_client.get("/authors/")  # Выполняем GET-запрос на эндпоинт "/authors/"
    assert response.status_code == 200  # Проверяем, что статус-код ответа равен 200 (OK)
    assert len(response.json()) > 0  # Проверяем, что список авторов не пуст


@pytest.mark.asyncio  # Маркируем тест как асинхронный
async def test_get_author_by_id(async_client):
    """
    Тест для проверки получения автора по ID.
    """
    response = await async_client.get("/authors/1")  # Выполняем GET-запрос на эндпоинт "/authors/1"
    assert response.status_code == 200  # Проверяем, что статус-код ответа равен 200 (OK)
    assert response.json()["id"] == 1  # Проверяем, что ID автора в ответе равен 1


@pytest.mark.asyncio  # Маркируем тест как асинхронный
async def test_update_author(async_client):
    """
    Тест для проверки обновления автора.
    """
    response = await async_client.put("/authors/1",
                                      json={  # Выполняем PUT-запрос на эндпоинт "/authors/1" с JSON-данными
                                          "first_name": "Jane",
                                          "last_name": "Doe",
                                          "birth_date": "1980-01-01"
                                      })
    assert response.status_code == 200  # Проверяем, что статус-код ответа равен 200 (OK)
    assert response.json()["first_name"] == "Jane"  # Проверяем, что имя автора в ответе соответствует обновленному


@pytest.mark.asyncio  # Маркируем тест как асинхронный
async def test_delete_author(async_client):
    """
    Тест для проверки удаления автора.
    """
    response = await async_client.delete("/authors/1")  # Выполняем DELETE-запрос на эндпоинт "/authors/1"
    assert response.status_code == 200  # Проверяем, что статус-код ответа равен 200 (OK)
    response = await async_client.get("/authors/1")  # Выполняем GET-запрос на эндпоинт "/authors/1" после удаления
    assert response.status_code == 404  # Проверяем, что статус-код ответа равен 404 (Not Found), так как автора быть не должно
