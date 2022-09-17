import os
from PIL import Image
from PyPDF2 import PdfReader, PdfMerger, PdfWriter
import download
import shutil


def conv_rgba_to_rgb(file: str) -> Image.Image:
    rgba = Image.open(file)
    rgb = Image.new("RGB", rgba.size, (255, 255, 255))
    rgb.paste(rgba)
    return rgb


def download_chapter_pdfs(start, end, name):
    page_len = download.download_chapters(start, end)
    merger = PdfMerger()
    for chapter, lenght in page_len.items():
        images = [conv_rgba_to_rgb(f"{chapter}\\{i}.jpg") for i in range(lenght)]
        images[0].save(f"{chapter}.pdf", "PDF", append_images=images[1:], save_all=True)
        merger.append(f"{chapter}.pdf", f"{chapter}")
    merger.write(f"{name}.pdf")
    merger.close()
    for chapter in page_len.keys():
        os.remove(f"{chapter}.pdf")
        shutil.rmtree(f"{str(chapter)}")


def add_pdf(file: str, chapter: int):
    lenght = download.download_chapters(chapter)
    images = [conv_rgba_to_rgb(f"{chapter}\\{i}.jpg") for i in range(lenght)]
    images[0].save(f"{chapter}.pdf", "PDF", append_images=images[1:], save_all=True)
    merger = PdfMerger()
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.getOutlines()
    merger.append(f"{file}.pdf")
    merger.append(f"{str(chapter)}.pdf", f"{chapter}")
    for outline in outlines:
        merger.add_bookmark(outline["/Title"], outline["/Page"])
    merger.write(f"{file}+{str(chapter)}.pdf")
    merger.close()
    shutil.rmtree(f"{str(chapter)}")
    os.remove(f"{file}.pdf")


def download_pdf_chapter(chapter: int):
    lenght = download.download_chapters(chapter)
    images = [conv_rgba_to_rgb(f"{chapter}\\{i}.jpg") for i in range(lenght)]
    images[0].save(f"temp.pdf", "PDF", append_images=images[1:], save_all=True)
    reader = PdfReader(f"temp.pdf")
    writer = PdfWriter()
    for page in range(lenght):
        writer.addPage(reader.getPage(page))
    writer.addBookmark(str(chapter), 0)
    writer.write(f"{chapter}.pdf")
    os.remove("temp.pdf")
    shutil.rmtree(str(chapter))


def last_chapter_in_pdf(file: str, last_chapter: int):
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.outlines
    chapter = int(outlines[-1]["/Title"])
    if last_chapter == chapter:
        return True
    else:
        return False


def get_last_chapter() -> int:
    lista = download.list_chapter_link()
    link = lista[-1]
    chapter = link.split("-")[-1]
    return int(chapter)

def next_chapter(file: str) -> int:
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.getOutlines()
    return max(int(outline["/Title"]) for outline in outlines) + 1


def previous_chapter(file: str) -> int:
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.getOutlines()
    return min(int(outline["/Title"]) for outline in outlines) - 1


def add_pdf_begin(file: str, chapter: int):
    lenght = download.download_chapters(chapter)
    images = [conv_rgba_to_rgb(f"{chapter}\\{i}.jpg") for i in range(lenght)]
    images[0].save(f"{chapter}.pdf", "PDF", append_images=images[1:], save_all=True)
    merger = PdfMerger()
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.getOutlines()
    merger.append(f"{chapter}.pdf")
    merger.append(f"{file}.pdf")
    merger.add_bookmark(str(chapter), 0)
    for outline in outlines:
        merger.add_bookmark(outline["/Title"], int(outline["/Page"]) + lenght)
    merger.write(f"{chapter}+{file}.pdf")
    merger.close()
    os.remove(f"{chapter}.pdf")
    shutil.rmtree(str(chapter))
