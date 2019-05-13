from tkinter import *
from PIL import ImageTk, Image
import numpy as np

class Receiver:

    sum = 0

    def __init__(self):
        i = Image.open('Spike.png')
        self.receiverArray = np.array(i)

    frame = []

    def receiveImage(self, frame, index, SumBefore):
        self.frame = frame
        self.receiverArray[index] = frame
        for i in range (0,10):
            for j in range (0,4):
                self.sum += self.receiverArray[index][i][j] + i*4 + j*2
        if self.sum == SumBefore:
            return True
        else:
            return False

