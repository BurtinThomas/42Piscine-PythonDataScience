import numpy
from PIL import Image

def ft_zoom(img: Image.Image):
    zoomed_img = img.crop((400, 100, 800, 500))
    zoomed_img = zoomed_img.convert("L")
    return numpy.array(zoomed_img)