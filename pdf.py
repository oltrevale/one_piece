from PIL import Image
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfMerger
import main
def crea_pdf(start,end):
    dizionario = main.scarica_piu_capitoli(start,end)
    print(dizionario)
    for capitolo,lunghezza in dizionario.items():
        images = [Image.open(f'{capitolo}\\{indice}.jpg')for indice in range(lunghezza)]
        images[0].save(f'{capitolo}.pdf',
        "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    merge=PdfMerger()
    for capitolo in range(start,end+1):
        merge.append(PdfFileReader(f'{capitolo}.pdf'),'rb')
    merge.write('temp.pdf')
    writer = PdfFileWriter()# open output
    reader = PdfFileReader("temp.pdf")
    indice=0
    pagine_totali=sum(dizionario.values())
    print(pagine_totali)
    writer= PdfFileWriter()
    reader = PdfFileReader('temp.pdf')
    for i in range(pagine_totali):
        writer.addPage(reader.getPage(i))
    for capitolo,lunghezza in dizionario.items():
        writer.addBookmark(f'{capitolo}',indice)
        indice+=lunghezza
    with open(f'{start}-{end}.pdf','wb') as f:
        writer.write(f)
    


crea_pdf(1035,1037)