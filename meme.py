"""Meme Generator to execute from the Command-line."""


import os
import random
from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    if path is None:
        images = "./_data/photos/dog/"
        ima_ges = []
        for root, dirs, files in os.walk(images):
            ima_ges = [os.path.join(root, name) for name in files]

        img = random.choice(ima_ges)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="create a meme with body, "
                                                 "author and path!!")
    parser.add_argument('--body', type=str, default=None,
                        help="quote body to add to the image")
    parser.add_argument('--author', type=str, default=None,
                        help="add author of the text")
    parser.add_argument('--path', type=str, default=None,
                        help="file path to image")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
