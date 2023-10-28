from fastapi import APIRouter


router = APIRouter(
    prefix="/api/manga",
    tags=["manga"]
)

@router.get("/getAllMangas")
def get_all_mangas():
    pass

@router.get("/getRecentMangas")
def get_recent_mangas():
    pass