"""Define a quote model class."""


class QuoteModel:
    """Base class for a Quote."""

    def __init__(self, body, author: str) -> None:
        """Return a QuoteModel representation."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a QuoteModel string representation."""
        return f"{self.body} - {self.author}"
