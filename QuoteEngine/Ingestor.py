"""Module that Encapsulate modules."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .csvImporter import CSVImporter
from .docxImporter import DocxImporter
from .pdfImporter import PDFImporter
from .textImporter import TextImporter
from typing import List


class Ingestor(IngestorInterface):
    """Class encapsulating for the importer modules."""

    ingestors = [CSVImporter, DocxImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Ingest the file with the format ingestors."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
