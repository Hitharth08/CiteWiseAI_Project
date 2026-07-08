import fitz  # PyMuPDF
from docx import Document
from pathlib import Path


class DocumentParser:

    @staticmethod
    def read_pdf(file):
        """Extract text from PDF."""
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""

        for page_num, page in enumerate(doc):
            text += f"\n\n--- Page {page_num + 1} ---\n"
            text += page.get_text()

        return text

    @staticmethod
    def read_docx(file):
        """Extract text from DOCX."""
        document = Document(file)

        text = "\n".join(
            para.text for para in document.paragraphs
            if para.text.strip()
        )

        return text

    @staticmethod
    def read_txt(file):
        """Extract text from TXT."""
        return file.read().decode("utf-8")

    @staticmethod
    def parse(file):
        """Automatically detect and parse uploaded file."""

        extension = Path(file.name).suffix.lower()

        if extension == ".pdf":
            return DocumentParser.read_pdf(file)

        elif extension == ".docx":
            return DocumentParser.read_docx(file)

        elif extension == ".txt":
            return DocumentParser.read_txt(file)

        else:
            raise Exception(f"Unsupported file format: {extension}")