import os

from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfMerger
import main
import shutil

def conv_rgba_to_rgb(file) -> Image.Image:
    rgba = Image.open(file)
    rgb = Image.new("RGB", rgba.size, (255, 255, 255))
    rgb.paste(rgba)
    return rgb


def crea_pdf(start: int, end: int):
    dictionary = main.scarica_piu_capitoli(start, end)
    print(dictionary)
    for chapter, lenght in dictionary.items():
        images = [
            conv_rgba_to_rgb(f"Capitoli\\{chapter}\\{i}.jpg") for i in range(lenght)
        ]
        images[0].save(
            f"{chapter}.pdf", "PDF", append_images=images[1:], save_all=True
        )
    writer = PdfFileWriter()
    i = 0
    for chapter, lenght in dictionary.items():
        reader = PdfFileReader(f"{chapter}.pdf")
        for pagina in range(lenght):
            writer.add_page(reader.getPage(pagina))
        writer.addBookmark(f"{chapter}", i)
        i = i +lenght

    with open(f"{start}-{end}.pdf", "wb") as f:
        writer.write(f)
    for chapter in range(start, end+1):
        os.remove(f'{chapter}.pdf')
        shutil.rmtree(f'Capitoli\\{chapter}')


crea_pdf(1042, 1044)
