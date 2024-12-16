import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Определяем путь к .env файлу
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Загружаем переменные окружения из .env файла
load_dotenv(ENV_PATH)

# Получаем переменные из окружения (они были загружены из .env)
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# Чтение URL базы данных из переменных окружения
DATABASE_URL_SQLALCHEMY = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}/{db_name}"

if not DATABASE_URL_SQLALCHEMY:
    raise ValueError("DATABASE_URL не задан в файле .env")

# Создание движка и сессий SQLAlchemy
Base = declarative_base()
engine = create_async_engine(DATABASE_URL_SQLALCHEMY)


# Генератор для получения сессии базы данных
async def get_db():
    async with AsyncSession(engine) as session:
        yield session
