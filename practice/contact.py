import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from SRC.pdf_extractor import extract_text
from SRC.text_cleaner import clean_text
from SRC.information_extractor import extract_information


document = "D:\\PROJECTS\\AI RESUME SCANNER\\DATA\\resume.pdf"

text = extract_text(document)

cleaned_text = clean_text(text)

information = extract_information(cleaned_text)

print(information)