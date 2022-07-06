from PyPDF2 import PdfReader, PdfWriter, PdfMerger

reader = PdfReader(input("Pdf File Location:"))

def Read(txt):
    meta, txt, page = reader.metadata, txt.replace('end', str(len(reader.pages))).split(), []
    print(f"{meta.title}\n{meta.author}\n{meta.subject}\n{meta.creator}\n{meta.producer}")
    if 'metadata' != txt: 
        for i in txt: 
            if i.isnumeric(): page.append(int(i))
    for i in range(page[0]-1, page[-1]): print(reader.pages[i].extract_text())

def WriteMetaLock():
    writer = PdfWriter()
    for page in reader.pages: # Add all pages to the writer
        writer.add_page(page)
    if 'write' in txt:
        writer.add_metadata( 
        {
             "/Author": "Martin",
             "/Producer": "Libre Writer",
             })
    elif reader.is_encrypted:
        reader.decrypt(input('Enter set password:'))
        for page in reader.pages: # Add all pages to the writer
            writer.add_page(page)
    else:  writer.encrypt(input('set a password:')) # Add a password to the new PDF
    with open(input("New File Name:"), "wb") as f: # Save the new PDF to a file
        writer.write(f)

def MergePdf():
    merger = PdfMerger()
    for pdf in [input("Location of file 1:"), input("Location of file 2:"), input("Location of file 3:")]:
        merger.append(pdf)
    merger.write(input("New File Name:"))
    merger.close()

