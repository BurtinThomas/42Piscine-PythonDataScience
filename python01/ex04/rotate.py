import numpy
from PIL import Image

def ft_rotate(arrayImgZoom):
    
    img = Image.fromarray(arrayImgZoom)
    width, height = img.size
    transposed_image = Image.new("L", (height, width))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            transposed_image.putpixel((y, x), pixel)

    return numpy.array(transposed_image)
