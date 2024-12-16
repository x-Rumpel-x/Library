from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app import models, schemas


# Получение всех записей из указанной модели
async def get_all(model, db: AsyncSession):
    # Выполняем SELECT запрос ко всем записям модели
    result = await db.execute(select(model))
    # Возвращаем все записи в виде списка объектов
    return result.scalars().all()


# Получение записи по ID из указанной модели
async def get_by_id(model, id: int, db: AsyncSession):
    # Выполняем SELECT запрос с условием поиска по ID
    result = await db.execute(select(model).where(model.id == id))
    # Возвращаем одну запись или None, если запись не найдена
    return result.scalar_one_or_none()


# Создание новой записи в базе данных
async def create_entry(model, data: dict, db: AsyncSession):
    # Создаем экземпляр модели, передавая данные из словаря
    entry = model(**data)
    # Добавляем запись в сессию
    db.add(entry)
    # Подтверждаем изменения (фиксируем их в базе данных)
    await db.commit()
    # Обновляем запись с учетом её состояния в базе данных
    await db.refresh(entry)
    # Возвращаем созданную запись
    return entry


# Обновление существующей записи в базе данных
async def update_entry(model, id: int, data: dict, db: AsyncSession):
    # Ищем запись по ID
    entry = await get_by_id(model, id, db)
    if not entry:
        # Если запись не найдена, выбрасываем исключение
        raise NoResultFound
    # Обновляем поля записи на основе переданных данных
    for key, value in data.items():
        setattr(entry, key, value)
    # Подтверждаем изменения
    await db.commit()
    # Возвращаем обновленную запись
    return entry


# Удаление записи из базы данных
async def delete_entry(model, id: int, db: AsyncSession):
    # Ищем запись по ID
    entry = await get_by_id(model, id, db)
    if not entry:
        # Если запись не найдена, выбрасываем исключение
        raise NoResultFound
    # Удаляем запись из базы данных
    await db.delete(entry)
    # Подтверждаем изменения
    await db.commit()
    # Возвращаем удаленную запись (обычно для подтверждения удаления)
    return entry
