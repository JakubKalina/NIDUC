from tkinter import *
from PIL import ImageTk, Image
import numpy as np

class Sender:

    # Tablica ramki
    senderArray = []

    def LoadImage(self):
        i = Image.open('Spike.png')
        self.senderArray = np.array(i)

    def SendFrame(self, index):
        return self.senderArray[index]

