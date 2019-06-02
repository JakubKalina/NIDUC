from tkinter import *
from PIL import ImageTk, Image
import numpy
import zlib
import binascii

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

#funkcja tworzy tablice ramek o podanym rozmiarze oraz dodaje wybrana wczesniej sume kontrolna
def gruop_into_frames(image, size,ChosenSumAlgorithm):
        counter = 0
        b = 0
        number = 0
        row = []
        tableOfFrames = []
        # dzieli obraz na ramki gotowe do przesłania
        while counter < len(image)-1:
            if b < size:
                row.append(image[counter])
                b = b + 1
                counter += 1
            else:
                # generowanie sumy kontrolnej algorytmem Luhna
                if ChosenSumAlgorithm == 1:
                    row = add_control_sum_LuhnAlgorithm(row)
                if ChosenSumAlgorithm == 2:
                    row = add_control_sum_CRC(row)
                if ChosenSumAlgorithm == 3:
                    row = add_parity_bit(row)
                tableOfFrames.append(row)
                row = []
                b = 0
            if counter == len(image) - 1:
                sum = 0
                for k in range(0, len(row)):
                    help = row[k]
                    while help > 0:
                        sum += help % 10
                        help = int(help / 10)
                sum = sum % 10
                sum = 10 - sum
                row.append(sum)
                tableOfFrames.append(row)
                counter += 1
        return tableOfFrames

def add_control_sum_LuhnAlgorithm(frame):
    control_sum = 0
    for k in range(0, len(frame)):
        helper = frame[k]
        while helper > 0:
            control_sum += helper % 10
            helper = int(helper / 10)
    control_sum = control_sum % 10
    control_sum = 10 - control_sum
    frame.append(control_sum)
    return frame

def add_control_sum_CRC(frame):
    text = ''
    for i in range(0, len(frame)):
        text += str(frame[i])
    crchex = hex(zlib.crc32(bytes(text, 'utf-8')))
    frame.append(crchex)
    return frame

def add_parity_bit(frame):
    count_1 = 0
    for i in range(0,len(frame)):
        helper = frame[i]
        while helper > 0:
            pom = helper % 2
            helper = int(helper/2)
            if pom == 1:
                count_1 += 1
    if count_1 % 2 == 1:
        frame.append(1)
    else:
        frame.append(0)
    print(frame)
    return frame
