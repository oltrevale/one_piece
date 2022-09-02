import requests
from bs4 import BeautifulSoup


def restitusci_nome_pagina(capitolo: int, pagina: int) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
    }
    link = (
        f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{capitolo}/page/{pagina}"
    )
    text = requests.get(link).text
    soup = BeautifulSoup(text, "html.parser")
    img = soup.find(class_="open open_image")
    return img["src"]


def restituisci_pagine(capitolo: int) -> tuple[list, int]:
    lista = [restitusci_nome_pagina(capitolo, i) for i in range(2, 23)]
    return lista, len(lista)


def scarica_piu_capitoli(start, end) -> dict:
    dizionario = {}
    import os

    for capitolo in range(start, end + 1):
        try:
            os.makedirs(f'Capitoli')
        except:
            pass
        try:
            os.makedirs(f"Capitoli\\{capitolo}")
        except:
            pass

        lista, lunghezza = restituisci_pagine(capitolo)
        dizionario[capitolo] = lunghezza
        for i, link in enumerate(lista):
            with open(f"Capitoli\\{capitolo}\\{i}.jpg", "wb") as f:
                f.write(requests.get(link).content)
    return dizionario
