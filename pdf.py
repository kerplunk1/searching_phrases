from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

def get_text(path_to_pdf_life):
    try:
        reader = PdfReader(path_to_pdf_life)
        text_from_each_pages = []
        for page in reader.pages:
            text_from_one_page = page.extract_text().replace('\n', '')
            text_from_each_pages.append(text_from_one_page)
        all_text = ''.join(text_from_each_pages)
        return all_text
    except PdfReadError:
        return "Ошибка чтения PDF-файла"

