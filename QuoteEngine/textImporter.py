"""Ingestor class for txt files."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List


class TextImporter(IngestorInterface):
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception("no txt-file available")

        quotes = []

        with open(path, "r", encoding='utf-8-sig') as txt:
            for index, line in enumerate(txt):
                parse = line.strip().split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes
