import os
from PIL import Image, UnidentifiedImageError
from PyPDF2 import PdfReader, PdfMerger, PdfWriter
import download
import shutil


def conv_rgba_to_rgb(file: str) -> Image.Image:
    rgba = Image.open(file)
    rgb = Image.new("RGB", rgba.size, (255, 255, 255))
    rgb.paste(rgba)
    return rgb


def download_chapter_pdfs(start: int, end: int, name: int | str):
    if os.path.isfile(f"{name}.pdf"):
        print("file is already downloaded")
    else:
        if start != end:
            page_len = download.download_chapters(start, end)
            merger = PdfMerger()
            for chapter, length in page_len.items():
                files = [f"{chapter}\\{i}.jpg" for i in range(length)]
                try:

                    images = [conv_rgba_to_rgb(file) for file in files]

                except:
                    images = []
                    for file in files:
                        try:
                            image = conv_rgba_to_rgb(file)
                            images.append(image)
                        except UnidentifiedImageError:
                            pass
                images[0].save(
                    f"{chapter}.pdf", "PDF", append_images=images[1:], save_all=True
                )

                shutil.rmtree(f"{str(chapter)}")
                print(f"\n{chapter} converted in pdf")
                merger.append(f"{chapter}.pdf", f"{chapter}")
            merger.write(f"{name}.pdf")
            merger.close()

        else:
            page_len = download.download_chapters(start, end)
            files = [f"{start}\\{i}.jpg" for i in range(page_len[start])]
            try:

                images = [conv_rgba_to_rgb(file) for file in files]
            except:
                images = []
                for file in files:
                    try:
                        image = conv_rgba_to_rgb(file)
                        images.append(image)
                    except:
                        print("lost a image")
            images[0].save(f"temp.pdf", "PDF", append_images=images[1:], save_all=True)
            reader = PdfReader(f"temp.pdf")
            writer = PdfWriter()
            for page in range(len(images)):
                writer.addPage(reader.getPage(page))
            writer.addBookmark(str(start), 0)
            writer.write(f"{start}.pdf")
            os.remove("temp.pdf")
            shutil.rmtree(str(start))
    print(f"{name}.pdf file created")


def get_last_chapter() -> int:
    lista = download.list_chapter_link()
    link = lista[-1]
    chapter = link.split("-")[-1]
    return int(chapter)


def is_last_chapter_in_pdf(file: str, last_chapter: int) -> bool:
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.outlines
    chapter = int(outlines[-1]["/Title"])
    if last_chapter == chapter:
        return True
    else:
        return False


def get_next_chapter(file: str) -> int:
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.getOutlines()
    return max(int(outline["/Title"]) for outline in outlines) + 1


def get_previous_chapter(file: str) -> int:
    reader = PdfReader(f"{file}.pdf")
    outlines = reader.getOutlines()
    return min(int(outline["/Title"]) for outline in outlines) - 1


def merge_pdf(file: str | int, file2: str | int, name: str | int):
    if os.path.isfile(f"{name}.pdf"):
        print("file is already downloaded")
    else:
        reader = PdfReader(f"{file}.pdf")
        reader2 = PdfReader(f"{file2}.pdf")
        num_pages = reader.getNumPages()
        outlines = reader.getOutlines()
        outlines2 = reader2.getOutlines()
        merger = PdfMerger()
        merger.append(f"{file}.pdf")
        merger.append(f"{file2}.pdf")
        for outline in outlines:
            merger.add_bookmark(outline["/Title"], outline["/Page"])
        for outline in outlines2:
            merger.add_bookmark(outline["/Title"], outline["/Page"] + num_pages)
        merger.write(f"{name}.pdf")
        merger.close()
        print(f"{name}.pdf created")
