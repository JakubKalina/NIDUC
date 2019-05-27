import Image as ImageLib
from Interference import interfere
from Sender import Sender
from Receiver import Receiver
import numpy
import threading

# deklaracja potrzebnych zmiennych globalnych
#       - najlepiej żeby nie były to dane które mają zostać/powinny byc przesłane
width = 14
height = 14
cell_width = 3
receiver = Receiver()
sender = Sender(receiver=receiver)
receiver.set_sender(sender=sender)
chosenOption = 0

#wysw obraz zwykly
ImageLib.display_original_image(height, width)

#zepsuj
#array = interfere(ImageLib.image_to_array(ImageLib.load_image()))
array = ImageLib.image_to_array(ImageLib.load_image())

print("podaj wielkosc ramki")
Sender.size = int(input())
print("podaj wielkosc okna")
Sender.windowSize = int(input())

receiver.frameSize = Sender.size
Sender.image = array

# wybór odpowiedniego protokołu
print("Wybierz protokół do przesyłu danych")
print("1. Stop And Wait")
print("2. Go Back N")
print("3. Selective Repeat")
chosenOption = int(input())

if (chosenOption == 1):
    print("1")
if (chosenOption == 2):
    print("2")
if (chosenOption == 3):
    threading.Thread(target=Sender.send_frame_selective(Sender)).start()
    receiver.receiver_frame()


array = numpy.asarray(receiver.receivedArray)
array = ImageLib.unflatten_array(array, width, cell_width)

#wysw zepsuty
ImageLib.display_image(array, height=height, width=width)
