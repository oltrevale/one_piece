import requests
from bs4 import BeautifulSoup


def restitusci_nome_pagina(capitolo: int, pagina: int) -> str:
    link = (
        f"https://www.juinjutsureader.ovh/read/one-piece/it/0/{capitolo}/page/{pagina}"
    )
    text = requests.get(link).text
    soup = BeautifulSoup(text, "html.parser")
    img = soup.find(class_="open open_image")
    return img["src"]


def restituisci_pagine(capitolo: int) -> list:
    lista = [restitusci_nome_pagina(capitolo, i) for i in range(2, 23)]
    return lista,len(lista)
def scarica_piu_capitoli(start,end):
    dizionario={}
    import os 
    for capitolo in range(start,end+1):
        try:
            os.makedirs(f'{capitolo}')
        except:
            pass
        
        lista,lunghezza=restituisci_pagine(capitolo)
        dizionario[capitolo]=lunghezza
        for i, link in enumerate(lista):
            with open(f"{capitolo}\\{i}.jpg", "wb") as f:
                f.write(requests.get(link).content)
    return dizionario 
