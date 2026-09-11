import pymupdf 

pdf = pymupdf.open("practice/resume.pdf")

text =""

for page in pdf:
    text += page.get_text()

pdf.close()

print(text)
