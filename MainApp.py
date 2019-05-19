from Resources.protocols.StopAndWait import StopAndWait
from Resources.Sender import Sender
from Resources.Receiver import Receiver
import Resources.Image as ImageLib
from Resources.Interference import interfere

# deklaracja potrzebnych zmiennych globalnych
#       - najlepiej żeby nie były to dane które mają zostać/powinny byc przesłane

# sender = Sender(protocol=StopAndWait())

# Aplikacja startowa

# wyświetl obraz przed wysłaniem
ImageLib.display_original_image(14, 14)
# zakłócanie
array = interfere(ImageLib.image_to_array(ImageLib.load_image()))
# składanie tablicy jednowymiarowej do formatu tablicy konwertowalnej do obrazu(3 wymiarowej)
array = ImageLib.unflatten_array(array, 14, 3)
# wyświetlanie zakłócanego obrazu
ImageLib.display_image(array, 14, 14)
