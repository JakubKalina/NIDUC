from Resources.protocols.GoBackN import GoBackN
from Resources.Sender import Sender
from Resources.Receiver import Receiver
import Resources.Image as ImageLib
from Resources.Interference import interfere
import time

# deklaracja potrzebnych zmiennych globalnych
#       - najlepiej żeby nie były to dane które mają zostać/powinny byc przesłane
width = 14
height = 14
cell_width = 3
object_size = width * height * cell_width

receiver = Receiver()
sender = Sender(receiver=receiver)
receiver.set_sender(sender=sender)
# SKRYPT GŁÓWNY

# wyświetl obraz przed wysłaniem

# ImageLib.display_original_image(height, width)

# zakłócanie
array = ImageLib.image_to_array(ImageLib.load_image())
array = interfere(array)

#  - - - PRZESYŁANIE - - -

# array = numpy.asarray([1, 2, 3, 4, 5, 6])
goBackN = GoBackN(sender=sender, receiver=receiver, window_size=50, array_size=object_size)
goBackN.delay = 0
goBackN.start_transmission(array)


new_array = ImageLib.unflatten_array(array, width, cell_width)

ImageLib.display_image(new_array, height=height, width=width)
