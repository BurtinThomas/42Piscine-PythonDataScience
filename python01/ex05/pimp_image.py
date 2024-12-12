import numpy
from PIL import Image


def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    image = 255 - array
    Image.fromarray(image).show()


def ft_red(array):
    """
    Keeps only the red color channel of the image.
    """
    onlyRedChannel = array[:, :, 0]
    arrayRed = numpy.zeros_like(array)
    arrayRed[:, :, 0] = onlyRedChannel
    Image.fromarray(arrayRed).show()


def ft_green(array):
    """
    Keeps only the green color channel of the image.
    """
    onlyGreenChannel = array[:, :, 1]
    arrayGreen = numpy.zeros_like(array)
    arrayGreen[:, :, 1] = onlyGreenChannel
    Image.fromarray(arrayGreen).show()


def ft_blue(array):
    """
    Keeps only the blue color channel of the image.
    """
    onlyBlueChannel = array[:, :, 2]
    arrayBlue = numpy.zeros_like(array)
    arrayBlue[:, :, 2] = onlyBlueChannel
    Image.fromarray(arrayBlue).show()


def ft_grey(array):
    """
    Converts the image to grayscale.
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    arrayGrey = numpy.zeros_like(array)
    arrayGrey[:, :, 0] = grey_channel
    arrayGrey[:, :, 1] = grey_channel
    arrayGrey[:, :, 2] = grey_channel
    Image.fromarray(arrayGrey).show()
