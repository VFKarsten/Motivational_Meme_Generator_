"""Ingestor class for docx files."""

from docx import Document
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List


class DocxImporter(IngestorInterface):
    """Ingest the docx file."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception("no docx-file available")

        doc = Document(path)
        quotes = []
        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes
