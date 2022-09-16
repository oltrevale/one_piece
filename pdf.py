import os
from PIL import Image
from PyPDF2 import  PdfReader,PdfMerger
import main
import shutil

def conv_rgba_to_rgb(file) -> Image.Image:
    rgba = Image.open(file)
    rgb = Image.new("RGB", rgba.size, (255, 255, 255))
    rgb.paste(rgba)
    return rgb



def create_pdfs(start: int, end: int):
    dictionary = main.download_chapter(start, end)
    merger=PdfMerger()
    for chapter, lenght in dictionary.items():
        images = [
            conv_rgba_to_rgb(f"{chapter}\\{i}.jpg") for i in range(lenght)
        ]
        images[0].save(f"{chapter}.pdf", "PDF", append_images=images[1:], save_all=True)
        merger.append(f'{chapter}.pdf',f'{chapter}')
    merger.write(f'{start}-{end}.pdf')
    merger.close()
    for chapter in dictionary.keys():
        os.remove(f'{chapter}.pdf')

def add_pdf(chapter:int,file:str):
    lenght=main.download_chapter(chapter)
    crea_pdf(chapter,lenght)
    merger=PdfMerger()
    reader = PdfReader(f'{file}.pdf')
    outlines = reader.getOutlines()
    merger.append(f'{file}.pdf')
    merger.append(f'{str(chapter)}.pdf',f'{chapter}')
    for outline in outlines:
        merger.add_bookmark(outline['/Title'],outline['/Page'])
    merger.write(f'{file}+{str(chapter)}.pdf')
    merger.close()
    shutil.rmtree(f'{str(chapter)}')

