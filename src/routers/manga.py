from fastapi import APIRouter, HTTPException
from src.utils.scraper import get_recent_manga

router = APIRouter(
    prefix="/api/manga",
    tags=["manga"]
)

@router.get("/getAllMangas")
def get_all_mangas():
    pass

@router.get("/getRecentMangas")
def get_recent_mangas():
    try:
        return get_recent_manga()
    except:
        HTTPException(400, "Something went wrong")