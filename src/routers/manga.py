from fastapi import APIRouter, HTTPException
from starlette.responses import StreamingResponse
from ..utils.scraper import getHTML, get_manga_pages

router = APIRouter(
    prefix="/api/manga",
    tags=["manga"]
)

# /manga/page/[pagenumber]
@router.get("/page/{pagenumber}")
async def get_all_mangas(pagenumber: int):
    soup = await getHTML(f"https://www.brmangas.net/page/{pagenumber}/")

    try:
        container = soup.find_all("div", class_="listagem row")[-1]
    except:
        raise HTTPException(404, "Page not found")
    items = container.find_all("div", class_="item")

    mangas = []
    for item in items:
        title = item.find("h2", class_="titulo").text
        img = item.find("img")["original-src"]
        link = item.find("a")["href"]
        link = link.split("/")
        new_link = "/manga/detail/" + link[-2]

        mangas.append({
            "title": title,
            "img": img,
            "link": new_link
        })

    try:
        pagination = int(soup.find_all("a", class_="page-numbers")[-2].text)
    except IndexError:
        pagination = 0

    return {
        "results": mangas,
        "pagination": pagination
    }

# /manga/detail/[endpoint]
@router.get("/detail/{endpoint}")
async def manga_detail(endpoint: str):
    soup = await getHTML(f"https://www.brmangas.net/manga/{endpoint}/")

    try:
        title = soup.find("h1", class_="titulo text-uppercase").text

        description_container = soup.find("div", class_="serie-texto")
        description = description_container.find("p").text

        img_container = soup.find("div", class_="serie-capa")
        img = img_container.find("img")["src"]

        caps = soup.find_all("li", class_="row lista_ep")

        chapters = []
        for cap in caps:
            chapter = cap.find("a")
            link = chapter["href"]
            link = link.split("/")
            new_link = "/manga/read/" + link[-2]

            chapters.append({
                "chapter": chapter.text,
                "link": new_link
            })

        return {
            "title": title,
            "img": img,
            "description": description,
            "chapters": chapters
        }
    except:
        raise HTTPException(404, "non-existent manga")

# /manga/read/[endpoint]
@router.get("/read/{endpoint}")
def read_manga(endpoint: str):
    try:
        manga_name = "-".join(endpoint.split("-")[:-2])
        chapter = int(endpoint.split("-")[-2])
        initial = endpoint[0]
    except:
        raise HTTPException(404, "non-existent chapter")
    if initial.isnumeric(): initial = "numbers"

    return StreamingResponse(get_manga_pages(manga_name, initial, chapter))

# /search/[query]/[pagenumber]
@router.get("/search/{query}")
async def search_manga(query: str, pagenumber: int = 1):
    soup = await getHTML(f"https://www.brmangas.net/page/{pagenumber}/?s={query}")
    mangas = soup.find_all("div", class_="item")

    results = []
    for manga in mangas:
        img = manga.find("img")["src"]
        title = manga.find("h2", class_="titulo search").text
        link = manga.find("a")["href"]
        link = link.split("/")
        new_link = "/manga/detail/" + link[-2]

        results.append({
            "img": img,
            "title": title,
            "link": new_link
        })
    try:
        pagination = int(soup.find_all("a", class_="page-numbers")[-2].text)
    except IndexError:
        pagination = 0

    return {
        "results": results,
        "pagination": pagination
    }

# /genres
@router.get("/genres")
async def get_genres():
    # try:
    soup = await getHTML("https://www.brmangas.net/lista-de-generos-de-manga")
    genres_container = soup.find("div", class_="genres_page")
    genres = genres_container.find_all("li")
    genres = [genre.text for genre in genres]

    return {"genres": genres}
    # except Exception:
        # raise HTTPException(400, "Something went wrong")

# /genres/[endpoint]/[pagenumber]
@router.get("/genres/{endpoint}/{pagenumber}")
async def get_manga_of_the_genre(endpoint: str, pagenumber: int):
    soup = await getHTML(f"https://www.brmangas.net/category/{endpoint}/page/{pagenumber}/")

    mangas = soup.find_all("div", class_="item")
    results = []
    for manga in mangas:
        img = manga.find("img")["src"]
        title = manga.find("h2", class_="titulo").text
        link = manga.find("a")["href"]
        link = link.split("/")
        new_link = "/manga/detail/" + link[-2]

        results.append({
            "title": title,
            "img": img,
            "link": new_link
        })

    try:  
        pagination = int(soup.find_all("a", class_="page-numbers")[-2].text)
    except IndexError:
        pagination = 0

    return {
        "results": results,
        "pagination": pagination
    }


# /recommended
@router.get("/recommended")
async def recommended():
    try:
        soup = await getHTML("https://www.brmangas.net/")
        mangas = soup.find_all("div", class_="listagem row")

        results = []
        for manga in mangas[0]:
            img = manga.find("img")["original-src"]
            title = manga.find("h2", class_="titulo").text
            link = manga.find("a")["href"]
            link = link.split("/")
            new_link = "/manga/detail/" + link[-2]

            results.append({
                "img": img,
                "title": title,
                "link": new_link
            })

        return {"results": results}
    except Exception:
        raise HTTPException(400, "Something went wrong")