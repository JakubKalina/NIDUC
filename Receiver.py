from tkinter import *
from PIL import ImageTk, Image
import numpy as np

class Receiver:


    def __init__(self):
        i = Image.open('Spike.png')
        self.receiverArray = np.array(i)


    frame = []

    def receiveImage(self, frame, index):
        self.frame = frame
        self.receiverArray[index] = frame


    def DisplayImage(self, receivedArray):
        img = Image.fromarray(receivedArray)
        img.save('test.png')
        window = Tk()
        img = ImageTk.PhotoImage(Image.open("test.png"))
        panel = Label(window, image=img)
        panel.pack()
        window.mainloop()