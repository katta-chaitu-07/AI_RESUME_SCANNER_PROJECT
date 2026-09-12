import sys

sys.path.insert(0, r"D:\PROJECTS\AI RESUME SCANNER")

import os

print(os.getcwd())

import pymupdf
from SRC.pdf_extractor import extract_text
from SRC.text_cleaner import clean_text
from SRC.resume_parser import parse_resume

pdf = pymupdf.open(r"D:\PROJECTS\AI RESUME SCANNER\DATA\resume.pdf")

extract_text_pdf = extract_text(pdf)

print(extract_text_pdf)

print("\n")

cleaned_text = clean_text(extract_text_pdf)

print("Cleaned text \n ")
print(cleaned_text)

print("\n")

print("Resume parser ")
resume = parse_resume(cleaned_text)
print(resume)

