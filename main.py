import pdf
import sys
import os
import shutil

if sys.argv[1] == "addlast":
    chapter = pdf.get_last_chapter()
    try:
        if not pdf.last_chapter_in_pdf(sys.argv[2], chapter):
            pdf.add_pdf(sys.argv[2], chapter)
        else:
            print("last chapter already present")
    except FileNotFoundError:
        print(f"{sys.argv[2]} doesn t exits")
    except FileExistsError:
        try:
            os.remove(str(chapter))
            shutil.rmtree(str(chapter))
        except:
            shutil.rmtree(str(chapter))
        if not pdf.last_chapter_in_pdf():
            pdf.add_pdf(sys.argv[2], chapter)
        else:
            print("last chapter already present")

elif sys.argv[1] == "download":
    if len(sys.argv) == 3:
        try:
            pdf.download_pdf_chapter(int(sys.argv[2]))
        except FileExistsError:
            try:
                os.remove(f"{sys.argv[2]}.pdf")
                shutil.rmtree(sys.argv[2])
            except:
                shutil.rmtree(sys.argv[2])
            pdf.download_pdf_chapter(int(sys.argv[2]))
        except:
            print("type a downloadable chapter")
    elif len(sys.argv) == 4:
        try:
            pdf.download_chapter_pdfs(
                int(sys.argv[2]), int(sys.argv[3]), f"{sys.argv[2]}-{sys.argv[3]}"
            )
        except FileExistsError:
            for chapter in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
                try:
                    os.remove(f"{chapter}.pdf")
                    shutil.rmtree(str(chapter))
                except:
                    shutil.rmtree((str(chapter)))
            pdf.download_chapter_pdfs(
                int(sys.argv[2]), int(sys.argv[3]), f"{sys.argv[2]}-{sys.argv[3]}"
            )
        except:
            print("type range downloadable chapter like 400 500")
elif sys.argv[1] == "add":
    try:
        pdf.add_pdf(sys.argv[2], int(sys.argv[3]))
    except FileExistsError:
        try:
            os.remove(f"{sys.argv[2]}.pdf")
            shutil.rmtree(sys.argv[2])
        except:
            shutil.rmtree(sys.argv[2])

        pdf.add_pdf(sys.argv[2], int(sys.argv[3]))
    except FileNotFoundError:
        print(f"{sys.argv[2]} doesn t exits")
elif sys.argv[1] == "addnext":
    try:
        chapter = pdf.next_chapter(sys.argv[2])
        pdf.add_pdf(sys.argv[2], chapter)
    except FileExistsError:
        try:
            os.remove(f"{sys.argv[2]}.pdf")
            shutil.rmtree(sys.argv[2])
        except:
            shutil.rmtree(sys.argv[2])
        chapter = pdf.next_chapter(sys.argv[2])
        pdf.add_pdf(sys.argv[2], chapter)
    except FileNotFoundError:
        print(f"{sys.argv[2]} doesn t exits")

elif sys.argv[1] == "addprev":
    try:
        chapter = pdf.previous_chapter(sys.argv[2])
        pdf.add_pdf_begin(sys.argv[2], chapter)
    except FileNotFoundError:
        print(f"{sys.argv[2]} doesn t exits")
    except FileExistsError:
        try:
            os.remove(f"{chapter}.pdf")
            shutil.rmtree(str(chapter))
        except:
            shutil.rmtree(str(chapter))
        chapter = pdf.previous_chapter(sys.argv[2])
        pdf.add_pdf_begin(sys.argv[2], chapter)

else:
    print("type download,addlast,add,addnext,addprev")
