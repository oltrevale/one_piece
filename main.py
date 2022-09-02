import requests
from bs4 import BeautifulSoup


def return_link(chapter: int, page: int) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
    }
    link = f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{chapter}/page/{page}"
    text = requests.get(link).text
    soup = BeautifulSoup(text, "html.parser")
    img = soup.find(class_="open open_image")
    return img["src"]


def return_links(chapter: int) -> list[str]:
    return [return_link(chapter, i) for i in range(2, 23)]


def download_chapter(start, end) -> dict:
    dictionary = {}
    import os

    for chapter in range(start, end + 1):
        try:
            os.makedirs(f"Chapters")
        except:
            pass
        try:
            os.makedirs(f"Chapters\\{chapter}")
        except:
            pass

        links = return_links(chapter)
        dictionary[chapter] = len(links)
        for i, link in enumerate(links):
            with open(f"Chapters\\{chapter}\\{i}.jpg", "wb") as f:
                f.write(requests.get(link).content)
    return dictionary
