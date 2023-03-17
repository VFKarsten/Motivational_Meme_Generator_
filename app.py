import random
import os
import requests
from flask import Flask, render_template, request
from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for image in os.listdir(images_path):
        if image.endswith('.jpg'):
            imgs.append(os.path.join(images_path, image))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    body = request.form['body']
    author = request.form['author']
    image_url = request.form['image_url']
    get = requests.get(image_url, allow_redirects=True)

    image_name = random.randint(0, 100000000)
    tmp = f'./tmp/{image_name}.jpg'
    img = open(tmp, 'wb')
    img.write(get.content)
    img.close()
    picture = MemeEngine.MemeEngine('./static')
    path = picture.make_meme(tmp, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()