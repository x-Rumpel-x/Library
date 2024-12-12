from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models, crud
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Book)
async def create_author(author: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_entry(models.Book, author.dict(), db)


@router.get("/", response_model=list[schemas.Book])
async def read_authors(db: AsyncSession = Depends(get_db)):
    return await crud.get_all(models.Book, db)


@router.get("/{id}", response_model=schemas.Book)
async def read_author(id: int, db: AsyncSession = Depends(get_db)):
    author = await crud.get_by_id(models.Book, id, db)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.put("/{id}", response_model=schemas.Book)
async def update_author(id: int, author: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    return await crud.update_entry(models.Book, id, author.dict(), db)


@router.delete("/{id}")
async def delete_author(id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_entry(models.Book, id, db)
