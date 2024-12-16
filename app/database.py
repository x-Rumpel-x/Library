import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Определяем путь к .env файлу
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Загружаем переменные окружения из .env файла
load_dotenv(ENV_PATH)

# Чтение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не задан в файле .env")

# Создание движка и сессий SQLAlchemy
engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


# Генератор для получения сессии базы данных
async def get_db():
    async with SessionLocal() as session:
        yield session
