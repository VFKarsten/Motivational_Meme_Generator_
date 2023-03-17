"""Define a quote model class."""


class QuoteModel:
    """Base class for a Quote."""

    def __init__(self, body, author: str) -> None:
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a QuoteModel representation."""
        return f"{self.body} - {self.author}"
