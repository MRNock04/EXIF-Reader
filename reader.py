import numpy as np
import os
from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open('MUM_5432-Edit.jpg')
exif = image._getexif()

data = {}

for key, val in exif.items():
    if key in TAGS:
        data[TAGS[key]] = val

print(data['Software'])