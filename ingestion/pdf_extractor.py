import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_text_digital(path:str) -> str:
    results = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text=page.extract_text()
            if text:
                results += text
            tables = page.extract_table()
            if tables:
                for table in tables:
                    for row in table:
                        results += " | ".join(row) + "\n"
        return results
    
def extract_text_ocr(path:str) ->str:
    images = convert_from_path(path)
    results = ""
    for image in images :
        text = pytesseract.image_to_string(image)
        results += text
    return results

def extract (path:str) -> str:
    p=extract_text_digital(path)
    if p == "":
        p=extract_text_ocr(path)
    return p

    
    
