import pytest  # Импортируем библиотеку pytest для тестирования
from httpx import AsyncClient  # Импортируем AsyncClient из httpx для асинхронных HTTP-запросов
from app.main import app  # Импортируем FastAPI-приложение из модуля app.main
from app.database import engine, Base  # Импортируем движок базы данных и базовый класс моделей из app.database


@pytest.fixture(scope="module", autouse=True)  # Определяем фикстуру pytest, которая будет выполняться один раз на модуль, автоматически
async def setup_database():
    """
    Фикстура для настройки базы данных перед тестами и очистки после них.
    """
    async with engine.begin() as conn:  # Запускаем асинхронную транзакцию с движком БД
        await conn.run_sync(Base.metadata.drop_all)  # Удаляем все таблицы из БД, если они есть
        await conn.run_sync(Base.metadata.create_all)  # Создаем все таблицы, определенные в моделях
    yield  # Предоставляем управление тестовой функции
    async with engine.begin() as conn:  # Снова запускаем асинхронную транзакцию
        await conn.run_sync(Base.metadata.drop_all)  # Удаляем все таблицы из БД после выполнения тестов


@pytest.fixture(scope="module")  # Определяем фикстуру pytest, которая будет выполняться один раз на модуль
async def async_client():
    """
    Фикстура для создания асинхронного HTTP-клиента для тестирования API.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:  # Создаем асинхронный HTTP-клиент для тестирования, передавая приложение и базовый URL
        yield client  # Предоставляем HTTP-клиент тестовой функции