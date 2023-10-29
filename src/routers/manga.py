from fastapi import APIRouter, HTTPException
from src.utils.scraper import get_recent_manga, get_specific_manga as get_specific_manga_

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

@router.get("/getSpecificManga/{manga}")
async def get_specific_manga(manga: str):
    try:
        return get_specific_manga_(manga)
    except ValueError:
        raise HTTPException(400, "non-existent manga or irregular name")
    except Exception:
        raise HTTPException(400, "Something went wrong")