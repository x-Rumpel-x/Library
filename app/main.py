from fastapi import FastAPI
from app.routers import authors, books, borrows
from app.database import engine, Base

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(borrows.router, prefix="/borrows", tags=["Borrows"])
