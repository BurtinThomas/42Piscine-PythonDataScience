from load_image import ft_load
import numpy
import matplotlib.pyplot as plt


def main():
    try:
        image_array = ft_load("animal.jpeg")
        print(image_array)
        zoomed_img_array = image_array[100:500, 450:850, 0]
        zoomed_img_array = zoomed_img_array[:, :, numpy.newaxis]
        print(f"New shape after slicing: {zoomed_img_array.shape}")
        print(zoomed_img_array)
        plt.imshow(zoomed_img_array, cmap='gray')
        plt.xticks(numpy.arange(0, zoomed_img_array.shape[1], 50))
        plt.yticks(numpy.arange(0, zoomed_img_array.shape[0], 50))
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__} : {error}")
    except KeyboardInterrupt:
        print("\nInput interrupted. Exiting...")


if __name__ == "__main__":
    main()
