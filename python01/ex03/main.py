from load_image import ft_load
from zoom import ft_zoom
import numpy
from PIL import Image
import matplotlib.pyplot as plt

def printImage(imageArray, string):
    print(f"The new shape {string} is: {imageArray.shape}")
    print(imageArray)
    plt.imshow(imageArray, cmap='gray')
    plt.xticks(numpy.arange(0, imageArray.shape[1], 50))
    plt.yticks(numpy.arange(0, imageArray.shape[0], 50))
    plt.show()

def main():
    try:
        arrayImg = ft_load("animal.jpeg")
        arrayImgZoom = ft_zoom(Image.fromarray(arrayImg))
        printImage(arrayImgZoom, "after slicing")
    except Exception as error:
        print(f"{type(error).__name__} : {error}")

if __name__ == "__main__":
    main()