Meme Generator:
The software takes images and quotes as input and outputs a resized image. 

Dependencies:
Are listed in requirements.txt --> pip install -r requirements.txt
It is to install 'pdftotext' using the following link: https://pypi.org/project/pdftotext

Command Line Interface (CLI):
meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

web app:
python3 app.py

Modules
QuoteEngine:
The QuoteEngine module is responsible for importing quotes into the default quote library. 
The main feature is that it is capable of expanding to support new file types with relatively little modifications of code, by adding individual module files for each new file type.

MemeEngine:
The MemeEngine.py file contains an image manipulator class MemeEngine that can produce customized output, according to the class attribute parameters.

The project contains a TextIngestor, DocxIngestor, PDFIngestor and CSVIngestor class.
The classes inherits the IngestorInterface.

The project defines a MemeGenerator module with the following responsibilities:

Loading of a file from disk
Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
Add a caption to an image (string input) with a body and author to a random location on the image.
The class depends on the Pillow library to complete the defined, incomplete method signatures so that they work with JPEG/PNG files.

The method signature to make the meme should be: make_meme(self, img_path, text, author, width=500) -> str #generated image path
