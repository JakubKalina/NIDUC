from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import random

class Sender:

    # Tablica ramki
    senderArray = []
    imgWidth = 0
    imgHeight = 0
    sum = 0


    def LoadImage(self):
        i = Image.open('Spike.png')
        self.senderArray = np.array(i)
        # Oblicz SZEROKOŚC załadowanego zdjęcia [piksele]
        self.imgWidth = int(self.senderArray[0].size / 4)
        # Oblicz WYSOKOŚC załadowanego zdjęcia [piksele]
        self.imgHeight = int(self.senderArray.size / (4*self.imgWidth))


    def SendFrame(self, index):
        self.LoadImage()
        rando = random.randint(0,100)
        if rando > 90:
            DoNoise = True
        else:
            DoNoise = False
        if DoNoise:
            for i in range (0,10):
                for j in range (0,4):
                    self.senderArray[index][i][j] = 4
        return self.senderArray[index]

    def SendGoodFrame(self, index):
        self.LoadImage()
        return self.senderArray[index]

    def GenerateControlSum(self, index):
        self.LoadImage()
        self.sum = 0
        for i in range (0,10):
            for j in range (0,4):
                self.sum += self.senderArray[index][i][j] + i*4 + j*2
        return self.sum