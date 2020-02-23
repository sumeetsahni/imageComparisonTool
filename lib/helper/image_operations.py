#!/usr/bin/python

import math, operator
from PIL import Image
import logging


class ImageOperations():
    def __init__(self):
        logging.basicConfig(level=logging.getLevelName('INFO'))
        self.log = logging.getLogger(__name__)

    def compareimages(self, image1, image2):
        self.log.info("Image Comparison process started between image {} and image  {}".format(image1, image2))
        open_image1 = Image.open(image1)
        open_image2 = Image.open(image2)
        h1 = open_image1.histogram()
        h2 = open_image2.histogram()
        rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
        self.log.info("Image Comparison process completed between image {} and image  {}".format(image1, image2))
        return rms