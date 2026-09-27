from pathlib import Path
from pypdf import PdfReader


def load_pdfs(folder_path):

    documents = []

    for pdf_file in Path(folder_path).glob("*.pdf"):

        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append({
            "filename": pdf_file.name,
            "text": text
        })

    return documents