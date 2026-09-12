import pymupdf

def extract_text(document):


    pdf = pymupdf.open(document)

    text = ""

    for page in pdf:

        text += page.get_text() + "\n"

    pdf.close()

    return text    

