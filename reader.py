from PIL import Image
from PIL.TiffTags import TAGS
import pandas as pd

def get_date(image):
    """gets an image and returns the year and the month it was taken in 

    Args:
        image (str): the full path of the image

    Returns:
        year, month (str) : the year and month the image was taken in """    
    img = Image.open(image)
    date = img.tag[36867]

    year = date[0][0:4]
    month = date[0][5:7]
    day = date[0][8:10]

    return year, month, day

print(*get_date('MRN_1718.NEF'))