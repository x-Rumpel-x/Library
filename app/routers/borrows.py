from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models, crud
from app.database import get_db

router = APIRouter()


# Эндпоинт POST для создания новой записи о займе
@router.post("/", response_model=schemas.Borrow)
async def create_author(author: schemas.BorrowCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_entry(models.Borrow, author.dict(), db)


# Эндпоинт GET для получения списка всех записей о займах
@router.get("/", response_model=list[schemas.Borrow])
async def read_authors(db: AsyncSession = Depends(get_db)):
    return await crud.get_all(models.Borrow, db)


# Эндпоинт GET для получения конкретной записи о займе по ID
@router.get("/{id}", response_model=schemas.Borrow)
async def read_author(id: int, db: AsyncSession = Depends(get_db)):
    author = await crud.get_by_id(models.Borrow, id, db)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


# Эндпоинт PUT для обновления данных записи о займе по ID
@router.put("/{id}", response_model=schemas.Borrow)
async def update_author(id: int, author: schemas.BorrowCreate, db: AsyncSession = Depends(get_db)):
    return await crud.update_entry(models.Borrow, id, author.dict(), db)


# Эндпоинт DELETE для удаления записи о займе по ID
@router.delete("/{id}")
async def delete_author(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_entry(models.Borrow, id, db)
