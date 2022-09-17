import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}


def list_chapter_link() -> list[str]:
    link = "https://onepiecechapters.com/mangas/5/one-piece"
    html = requests.get(link).text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all(class_="block border border-border bg-card mb-3 p-3 rounded")
    links = [f"https://onepiecechapters.com{link['href']}" for link in links[::-1]]
    links = [link for link in links if link[-2] != "."]
    return links


def return_links(chapter: int) -> list[str]:
    lista = list_chapter_link()
    link = lista[chapter - 1]  # zero-index-based
    text = requests.get(link, headers=headers).text
    soup = BeautifulSoup(text, "html.parser")
    img = soup.find_all(class_="fixed-ratio-content")
    return [im["src"] for im in img]


def download_chapters(
    start_chapter: int, end_chapter: int | None = None
) -> dict[int, int] | int:
    import os

    if not end_chapter:
        os.makedirs(str(start_chapter))
        links = return_links(start_chapter)
        for i, link in enumerate(links):
            with open(f"{start_chapter}\\{i}.jpg", "wb") as f:
                f.write(requests.get(link).content)
        return len(links)
    else:
        page_len = {}
        for chapter in range(start_chapter, end_chapter + 1):
            os.makedirs(f"{chapter}")
            links = return_links(chapter)
            page_len[chapter] = len(links)
            for i, link in enumerate(links):
                with open(f"{chapter}\\{i}.jpg", "wb") as f:
                    f.write(requests.get(link).content)
        return page_len
