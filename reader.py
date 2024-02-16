from PIL import Image
from PIL.TiffTags import TAGS
import pandas as pd

img = Image.open('MRN_1930.NEF')
meta = {}

for key in img.tag:
    try: meta[str(TAGS[key])] = img.tag[key]
    except: pass

date = meta['DateTimeOriginal']

year = date[0][0:4]
month = date[0][5:7]
day = date[0][8:10]

print(year)
print(month)
print(day)