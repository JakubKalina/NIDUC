from Resources.protocols.StopAndWait import StopAndWait
from Resources.Sender import Sender
from Resources.Receiver import Receiver
import Resources.Image as ImageLib
from Resources.Interference import interfere

# deklaracja potrzebnych zmiennych globalnych
#       - najlepiej żeby nie były to dane które mają zostać/powinny byc przesłane
width = 14
height = 14
cell_width = 3

receiver = Receiver()
sender = Sender(receiver=receiver)
receiver.set_sender(sender=sender)
# Aplikacja startowa

# wyświetl obraz przed wysłaniem
ImageLib.display_original_image(height, width)
# zakłócanie
array = interfere(ImageLib.image_to_array(ImageLib.load_image()))

#  - - - PRZESYŁANIE - - -

stopAndWait = StopAndWait(sender=sender, receiver=receiver)

stopAndWait.start_transmission(array)

array = receiver.receivedArray

# składanie tablicy jednowymiarowej do formatu tablicy konwertowalnej do obrazu(3 wymiarowej)
array = ImageLib.unflatten_array(array, width, cell_width)
# wyświetlanie zakłócanego obrazu
ImageLib.display_image(array, height=height, width=width)
