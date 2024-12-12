from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app import models, schemas


async def get_all(model, db: AsyncSession):
    result = await db.execute(select(model))
    return result.scalars().all()


async def get_by_id(model, id: int, db: AsyncSession):
    result = await db.execute(select(model).where(model.id == id))
    return result.scalar_one_or_none()


async def create_entry(model, data: dict, db: AsyncSession):
    entry = model(**data)
    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry


async def update_entry(model, id: int, data: dict, db: AsyncSession):
    entry = await get_by_id(model, id, db)
    if not entry:
        raise NoResultFound
    for key, value in data.items():
        setattr(entry, key, value)
    await db.commit()
    return entry


async def delete_entry(model, id: int, db: AsyncSession):
    entry = await get_by_id(model, id, db)
    if not entry:
        raise NoResultFound
    await db.delete(entry)
    await db.commit()
    return entry
