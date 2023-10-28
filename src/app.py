from fastapi import FastAPI
from routers import manga


app = FastAPI(
    title="MangaKAI",
    description="Manga leitor",
    version="0.0.1",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.include_router(manga.router)