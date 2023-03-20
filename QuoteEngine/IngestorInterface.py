"""Module to specify abstract base classes."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for different types of files."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check if path(file) is insertable."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest the file with QuoteModels into path."""
        pass
