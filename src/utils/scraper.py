from bs4 import BeautifulSoup
import httpx
from requests_html import HTMLSession

async def getHTML(url) -> BeautifulSoup:
    session = HTMLSession()
    res = session.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


async def get_manga_pages(manga: str, initial: str, chapter: int):
    index = 1
    running = True
    true_url = -1
    while running:
        urls = [
            f"https://cdn.plaquiz.xyz/uploads/{initial}/{manga}/{chapter}/{index}",
            f"https://dn1.imgstatic.club/uploads/{initial}/{manga}/{chapter}/{index}"
            f"https://neogoog.xyz/uploads/{initial}/{manga}/{chapter}/{index}",
            f"https://viralcontentmxp.xyz/uploads/{initial}/{manga}/{chapter}/{index}",
        ]

        async with httpx.AsyncClient() as client:
            if true_url != -1:
                res = await client.get(urls[true_url])
            else:
                for i, url in enumerate(urls):
                    res = await client.get(url)
                    if res.status_code == 200:
                        true_url = i
                        break
                

        if res.status_code == 404:
            yield "finished application"
            continue
        index += 1
        yield urls[true_url]