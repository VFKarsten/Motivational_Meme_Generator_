"""Ingestor class for csv files."""

import pandas
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVImporter(IngestorInterface):
    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception("no csv-file available")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
