from load_image import ft_load
import numpy
import matplotlib.pyplot as plt


def transpose(np_array, rows, columns):
    transposed = []
    for i in range(columns):
        new_row = []
        for j in range(rows):
            new_row.append(np_array[j][i])
        transposed.append(new_row)
    return numpy.array(transposed)


def main():
    try:
        image_array = ft_load("animal.jpeg")
        zoomed_img_array = image_array[100:500, 450:850, 0]
        print(f"The shape of image is: {zoomed_img_array[:, :, numpy.newaxis].shape}")
        print(zoomed_img_array[:, :, numpy.newaxis])
        rotated_image = transpose(zoomed_img_array, zoomed_img_array.shape[0], zoomed_img_array.shape[1])
        print(f"New shape after Transpose: {rotated_image.shape}")
        print(rotated_image)
        plt.imshow(rotated_image, cmap='gray')
        plt.xticks(numpy.arange(0, rotated_image.shape[1], 50))
        plt.yticks(numpy.arange(0, rotated_image.shape[0], 50))
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__} : {error}")
    except KeyboardInterrupt:
        print("\nInput interrupted. Exiting...")


if __name__ == "__main__":
    main()
