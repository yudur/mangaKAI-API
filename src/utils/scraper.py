from bs4 import BeautifulSoup
import requests
from lxml import etree


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


def get_specific_manga(manga: str):
    manga = manga.replace(" ", "-")
    req = requests.get(f"https://mangaschan.net/manga/{manga.lower()}/")
    site = BeautifulSoup(req.text, "html.parser")
    dom = etree.HTML(str(site))

    try:
        title = site.find("h1", itemprop="name").text
    except:
        raise ValueError("non-existent manga or irregular name")

    status = dom.xpath(
        "/html/body/div[1]/div[2]/div/div[2]/article/div[1]/div[1]/div/div[4]/div[1]/i"
    )[0].text

    try:
        img = site.find("img", alt=title)["src"]
    except:
        try:
            img_container = site.find("div", itemprop="image")
            img = img_container.find("img")["src"]
        except:
            img = None

    description_container = site.find("div", itemprop="description")
    paragraphs_description = description_container.find_all("p")

    description = ""
    for paragraph in paragraphs_description:
        description = description + str(paragraph.text) + "\n"

    tags = site.find_all("a", rel="tag")
    tags = [tag.text for tag in tags]

    rating = site.find("div", itemprop="ratingValue")["content"]

    all_chapters = site.find_all("div", class_="eph-num")
    chapters = []
    for i, chapter in enumerate(all_chapters):
        if i == 0: continue

        link = chapter.find("a")["href"]
        _chapter = chapter.find("span", class_="chapternum").text
        release_date_of = chapter.find("span", class_="chapterdate").text

        chapters.append({
            "link": link,
            "chapter": _chapter,
            "releaseDateOf": release_date_of
        })

    return {
        "title": title,
        "description": description,
        "imageSrc": img,
        "tags": tags,
        "rating": rating,
        "status": status,
        "chapters": chapters
    }

if __name__=="__main__":
    # get_specific_manga("legend-of-the-northern-blade")
    get_specific_manga("amagami-san-chi-no-enmusubi-serie")