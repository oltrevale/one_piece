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
            f"{capitolo}.pdf",
            "PDF",
            append_images=images[1:],save_all=True
        )
    merge = PdfMerger()
    for capitolo in range(start, end + 1):
        merge.append(PdfFileReader(f"{capitolo}.pdf"), "rb")
    merge.write(f"prova_{start}-{end}.pdf")
    writer = PdfFileWriter()  # open output
    reader = PdfFileReader(f"prova_{start}-{end}.pdf")
    indice = 0
    pagine_totali = sum(dizionario.values())
    print(pagine_totali)
    writer = PdfFileWriter()
    reader = PdfFileReader(f"prova_{start}-{end}.pdf")
    for i in range(pagine_totali):
        writer.addPage(reader.getPage(i))
    for capitolo, lunghezza in dizionario.items():
        writer.addBookmark(f"{capitolo}", indice)
        indice += lunghezza
    with open(f"{start}-{end}.pdf", "wb") as f:
        writer.write(f)


crea_pdf(1045, 1046)
