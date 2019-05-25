from tkinter import *
from PIL import ImageTk, Image
from numpy import ndarray
import numpy

# Stała do wyświetlania większego obrazu (proporcjonalnego)
zoom = 30

# ścieżka do zdjęcia oryginalnego
ImagePath = "obraz.jpg"


# wyświetl obraz z tablicy(zagnieżdżonej)
def display_image(array, height, width):
    window = Tk()

    # oblicz proporcje obrazu
    ratio = height / width
    resize_width = width * zoom
    resize_height = int(resize_width * ratio)

    # tworzenie obrazu z tablicy
    image = Image.fromarray(array)
    image = image.resize((resize_width, resize_height))
    image = ImageTk.PhotoImage(image)
    panel = Label(window, image=image)
    panel.pack()
    window.mainloop()


# wyświetl ORYGINALNY obraz
def display_original_image(height, width):
    window = Tk()

    # oblicz proporcje obrazu
    ratio = height / width
    resize_width = width * zoom
    resize_height = int(resize_width * ratio)

    # tworzenie obrazu z tablicy
    image = Image.open(ImagePath)
    image = image.resize((resize_width, resize_height))
    image = ImageTk.PhotoImage(image)
    panel = Label(window, image=image)
    panel.pack()
    window.mainloop()


# utwórz jednowymiarową tablice z obrazu
def image_to_array(image):
    array_three_dimension = numpy.array(image)
    flatten_array = array_three_dimension.flatten('C')

    return flatten_array


# utwórz obiekt obrazu z podaje tablicy jednowymiarowej
def array_to_image(received_array):
    image = Image.fromarray(received_array)
    return image


# załaduj plik z grafiką
def load_image():
    image = Image.open(ImagePath)
    return image


# wyświetla tablice jednowymiarową, podzieloną na rzędy jak w obrazie
def print_image_array_values(array, image_width):
    row = array.size / image_width

    for i in range(0, array.size):
        if i % row == 0 and i != 0:
            print(f'{array[i]}, ')
            pass
        else:
            print(f'{array[i]}, ', end='')
            pass
        pass
    pass


def unflatten_array(array, width, cell_width):
    image_array = []
    cell = []

    for i in range(0, array.size):
        if (i + 1) % cell_width == 0:
            cell.append(array[i])
            # cell = numpy.asarray(cell)
            image_array.append(cell)
            cell = []
        else:
            cell.append(array[i])
        pass

    final_image_array = []
    image_array = numpy.asarray(image_array)

    row = []

    for j in range(0, int(image_array.size/cell_width)):
        if (j + 1) % width == 0:
            row.append(image_array[j])
            # row = numpy.asarray(row)
            final_image_array.append(row)
            row = []
        else:
            row.append(image_array[j])
        pass

    return numpy.asarray(final_image_array)
