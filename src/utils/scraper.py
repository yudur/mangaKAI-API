from bs4 import BeautifulSoup
import requests


def get_recent_manga() -> list:
    req = requests.get("https://mangaschan.net/ultimas-atualizacoes/")
    site = BeautifulSoup(req.text, "html.parser")

    containers = site.find_all("div", class_="uta")

    mangas = []
    for container in containers:
        img = container.find("img", class_="ts-post-image")
        title_manga = container.find("h4").text
        manga_status = container.find("span", class_="statusind Ongoing").text

        container_chapters = container.find_all("li")

        chapters = []
        for container_chapter in container_chapters:
            chapter = container_chapter.find("a")

            chapters.append({
                "chapter": chapter.text,
                "link": chapter["href"],
                "releaseDateOf": container_chapter.find("span").text
            })

        mangas.append({
            "imageSrc": img["data-src"],
            "title": title_manga,
            "mangaStatus": manga_status,
            "chapters": chapters
        })
    return mangas
