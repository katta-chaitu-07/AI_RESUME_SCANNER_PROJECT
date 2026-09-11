import pymupdf

def extract_text(document):


    pdf = pymupdf.open(document)

    text = ""

    for page in pdf:

        text += page.get_text() + "\n"

    return text    

info = extract_text(r"DATA/resume.pdf")

print(info)
