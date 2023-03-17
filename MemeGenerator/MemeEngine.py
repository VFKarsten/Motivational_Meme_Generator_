"""MemeEngine class is using Pillow. It generates memes to a 
determined directory. The supported image file types are jpg/png.
"""

import os
import random

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """ Instances of this class generated memes to a given director """
    def __init__(self, output_dir):
        """ Create the output directory path """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """ Generate a meme and provide the path of the file """
        img = Image.open(img_path)

        real_width, real_height = img.size
        height = int(real_height * width / real_width)
        img.thumbnail((width, height))

        # Select color and position to text view
        origin_1 = ImageFont.truetype("./_data/Origin/Helvetica-Normal.ttf", 25)
        origin_2 = ImageFont.truetype("./_data/Origin/Min-Sans.ttf", 20)
        charge = (0, 0, 0)
        text_position = random.choice(range(30, height - 50))

        # view the text on image
        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), text, charge, origin_1)
        draw.text((40, text_position + 25), f"- {author}", charge, origin_2)

        outfile = (self.output_dir + '/' + str(random.randint(0, 1000)) + '.jpg')

        img.save(outfile, "JPEG")
        return outfile

    @classmethod
    def MemeEngine(cls, param):
        pass
