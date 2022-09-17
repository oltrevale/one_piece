import pdf
import sys
import os
import shutil
if sys.argv[1]=='addlast':
    try:
        pdf.add_last_chapter(int(sys.argv[2]))
    except FileExistsError:
        try:
            os.remove(f'{sys.argv[2]}.pdf')
            shutil.rmtree(sys.argv[2])
        except:
            shutil.rmtree(sys.argv[2])
    pdf.add_last_chapter(int(sys.argv[2]))
            
elif sys.argv[1]=='download':
    if len(sys.argv)==3:
        try:
            pdf.download_pdf_chapter(int(sys.argv[2]))
        except FileExistsError:
            try:
                os.remove(f'{sys.argv[2]}.pdf')
                shutil.rmtree(sys.argv[2])
            except:
                shutil.rmtree(sys.argv[2])
        pdf.download_pdf_chapter(int(sys.argv[2]))
    elif len(sys.argv)==4:
        try:
            pdf.download_chapter_pdfs(int(sys.argv[2]),int(sys.argv[3]),f'{sys.argv[2]}-{sys.argv[3]}')
        except:
            for chapter in range(int(sys.argv[2]),int(sys.argv[3])+1):
                try:
                    os.remove(f'{chapter}.pdf')
                    shutil.rmtree(str(chapter))
                except:
                    shutil.rmtree((str(chapter)))
        pdf.download_chapter_pdfs(int(sys.argv[2]),int(sys.argv[3]),f'{sys.argv[2]}-{sys.argv[3]}')
elif sys.argv[1]=='add':
    try:
        pdf.add_pdf(sys.argv[2],int(sys.argv[3]))
    except FileExistsError:
        try:
            os.remove(f'{sys.argv[2]}.pdf')
            shutil.rmtree(sys.argv[2])
        except:
            shutil.rmtree(sys.argv[2]) 
        finally:
            pdf.add_pdf(sys.argv[2],int(sys.argv[3]))
    except FileNotFoundError:
        print('il file pdf a cui si cerca di aggiungere un capitolo non esiste')
elif sys.argv[1]=='addnext':
    chapter=pdf.next_chapter(sys.argv[2])
    try:
        pdf.add_pdf(sys.argv[2],int(sys.argv[3]))
    except FileExistsError:
        try:
            os.remove(f'{sys.argv[2]}.pdf')
            shutil.rmtree(sys.argv[2])
        except:
            shutil.rmtree(sys.argv[2]) 
        finally:
            pdf.add_pdf(sys.argv[2],int(sys.argv[3]))
    except FileNotFoundError:
        print('il file pdf a cui si cerca di aggiungere un capitolo non esiste')
    pdf.add_pdf(sys.argv[2],chapter)
elif  sys.argv[1]=='addprev':
    try:
        chapter=pdf.previous_chapter(sys.argv[2])
        pdf.add_pdf_start(sys.argv[2],chapter)
    except FileExistsError:
        try:
            os.remove(f'{chapter}.pdf')
            shutil.rmtree(str(chapter))
        except:
            shutil.rmtree(str(chapter)) 
        finally:
            pdf.add_pdf_start(sys.argv[2],chapter)
    except FileNotFoundError:
        print('il file pdf a cui si cerca di aggiungere un capitolo non esiste')
else:
    print('i comandi sono download,addlast,add,addnext,addprev')