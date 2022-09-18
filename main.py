import pdf
import sys


if sys.argv[1] == "addlast":
    last_chapter = pdf.get_last_chapter()
    if not pdf.last_chapter_in_pdf(sys.argv[2], last_chapter):
        pdf.download_chapter_pdfs(last_chapter, last_chapter, last_chapter)
        pdf.merge_pdf(sys.argv[2], last_chapter, f"{sys.argv[2]}+{last_chapter}")
    else:
        print("last chapter already present")

elif sys.argv[1] == "download":
    if len(sys.argv) == 3:
        try:
            pdf.download_chapter_pdfs(int(sys.argv[2]), int(sys.argv[2]), sys.argv[2])
        except ValueError:
            print("type a downloadable chapter")
    elif len(sys.argv) == 4:
        try:
            pdf.download_chapter_pdfs(
                int(sys.argv[2]), int(sys.argv[3]), f"{sys.argv[2]}-{sys.argv[3]}"
            )
        except ValueError:
            print("type range downloadable chapter like 400 500")
elif sys.argv[1] == "add":
    try:
        pdf.download_chapter_pdfs(int(sys.argv[3]), int(sys.argv[3]), int(sys.argv[3]))
        pdf.merge_pdf(sys.argv[2], sys.argv[3], f"{sys.argv[2]}+{sys.argv[3]}")
    except FileNotFoundError:
        print(f"{sys.argv[2]}.pdf doesn t exits")
elif sys.argv[1] == "addnext":
    try:
        next_chapter = pdf.get_next_chapter(sys.argv[2])
        pdf.download_chapter_pdfs(next_chapter, next_chapter, next_chapter)
        pdf.merge_pdf(sys.argv[2], next_chapter, f"{sys.argv[2]}+{next_chapter}")
    except FileNotFoundError:
        print(f"{sys.argv[2]}.pdf doesn t exits")

elif sys.argv[1] == "addprev":
    try:
        prev_chapter = pdf.get_previous_chapter(sys.argv[2])
        pdf.download_chapter_pdfs(prev_chapter, prev_chapter, prev_chapter)
        pdf.merge_pdf(str(prev_chapter), sys.argv[2], f"{prev_chapter}+{sys.argv[2]}")
    except FileNotFoundError:
        print(f"{sys.argv[2]}.pdf doesn t exits")
elif sys.argv[1] == "remuntada":
    last_chapter = pdf.get_last_chapter()
    try:
        if pdf.last_chapter_in_pdf(sys.argv[2], last_chapter):
            print("last chapter already exits in this file")
            quit()
        else:
            next_chapter = pdf.get_next_chapter(f"{sys.argv[2]}")
    except FileNotFoundError:
        print(f"{sys.argv[2]}.pdf doesn t exits")
        quit()
    except:
        "unable to retrieve number of this chapter"
        quit()
    if next_chapter == last_chapter:
        pdf.download_chapter_pdfs(next_chapter, last_chapter, f"{next_chapter}")
        pdf.merge_pdf(
            sys.argv[2],
            f"{next_chapter}",
            f"{sys.argv[2]}+{last_chapter}",
        )
    else:
        pdf.download_chapter_pdfs(
            next_chapter, last_chapter, f"{next_chapter}-{last_chapter}"
        )
        pdf.merge_pdf(
            sys.argv[2],
            f"{next_chapter}-{last_chapter}",
            f"{sys.argv[2]}-{last_chapter}",
        )

else:
    print("guide here https://github.com/oltrevale/one_piece")
