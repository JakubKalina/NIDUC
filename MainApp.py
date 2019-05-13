from tkinter import *
from numpy import half

from Sender import Sender
from Receiver import Receiver
from PIL import ImageTk, Image

width = 0
height = 0
zoom = 10

# Funkcja wyświetlająca obraz
def DisplayImage(receivedArray):
    window = Tk()
    image = Image.open("test.png")
    ratio = height / width
    img = Image.fromarray(receivedArray)
    #img.save('test.png')
    resizedWidth = width * zoom
    print(resizedWidth)
    resizedHeight = int(resizedWidth * ratio)
    image = img
    image = image.resize((resizedWidth,resizedHeight))
    img = ImageTk.PhotoImage(image)
    panel = Label(window, image=img)
    panel.pack()
    window.mainloop()

def DisplayImageGood():
    window = Tk()
    image = Image.open("test.png")
    ratio = height / width
    resizedWidth = width * zoom
    print(resizedWidth)
    resizedHeight = int(resizedWidth * ratio)
    image = image.resize((resizedWidth, resizedHeight))
    img = ImageTk.PhotoImage(image)
    panel = Label(window, image=img)
    panel.pack()
    window.mainloop()


# Obiekt nadajnika
sender = Sender()

# Obiekt odbiornika
receiver = Receiver()

# Załadowanie obrazu z pliku do tablicy
sender.LoadImage()

width = sender.imgWidth
print('Width: ',width)
height = sender.imgHeight
print('Height: ',height)

index = 0

while index < height:
    frame = sender.SendFrame(index)

    for i in range(0,width): # !!! W tym miejscu podmienić hieght na 0 aby byly kolory
        for j in range(0,3):
            frame[i][j] = 0

    receiver.receiveImage(frame, index)
    #print(receiver.frame)
    #print('\n')
    index = index + 1


# Wyświetlenie grafiki przed modyfikacją
DisplayImageGood()
# Wyświetlenie grafiki po modyfikacji
DisplayImage(receiver.receiverArray)


