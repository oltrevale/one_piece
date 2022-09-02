from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfMerger
import main


def crea_pdf(start, end):
    dizionario = main.scarica_piu_capitoli(start, end)
    print(dizionario)
    for capitolo, lunghezza in dizionario.items():
        images = [
            Image.open(f"{capitolo}\\{indice}.jpg") for indice in range(lunghezza)
        ]
        images[0].save(
            f"{capitolo}.pdf", "PDF", append_images=images[1:], save_all=True
        )
    writer=PdfFileWriter()
    indice=0
    for capitolo,lunghezza in dizionario.items():
        reader=PdfFileReader(f'{capitolo}.pdf')
        writer.addPage(reader.getPage(0))
        writer.addBookmark(f"{capitolo}", indice)
        indice+=lunghezza
        for i in range(1,lunghezza):
            writer.add_page(reader.getPage(i))
    with open(f"{start}-{end}.pdf", "wb") as f:
        writer.write(f)


crea_pdf(1036, 1037)
