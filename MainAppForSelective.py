from tkinter import *
import time
from SenderSelective import Sender
from ReceiverSelective import Receiver
from PIL import ImageTk, Image
import threading

width = 0
height = 0
zoom = 10
xd = True
frame = 0
index = 0
SumBefore = 0
List = []

# Funkcja wyświetlająca obraz
def DisplayImage(receivedArray):
    window = Tk()
    ratio = height / width
    img = Image.fromarray(receivedArray)
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

def Sending():
    global index,SumBefore,frame
    index = 0
    while index < height:
        SumBefore = sender.GenerateControlSum(index)
        frame = sender.SendFrame(index)
        time.sleep(0.5)
        index = index + 1
    index -= 1
    global xd
    xd = False

def Receiving():
    global xd,index,SumBefore,frame
    while xd:
        time.sleep(0.499)
        IsCorrect = receiver.receiveImage(frame, index, SumBefore)
        if IsCorrect ==100:
            print("poszlo")
        else:
            global List
            List.append(IsCorrect)
            print("nie poszlo")


def Checker():
    global List,SumBefore,frame
    while True:
        List2 = List
        time.sleep(0.3)
        if len(List2) > 0:
            for i in range (0,len(List2)):
                SumBefore = sender.GenerateControlSum(List2[i])
                frame = sender.SendFrame(List2[i])
                IsCorrect = receiver.receiveImage(frame, List2[i], SumBefore)
                if IsCorrect == 100:
                    List2.remove(List2[i])
                    i -= 1


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
threading.Thread(target=Sending).start()
threading.Thread(target=Receiving).start()
threading.Thread(target=Checker).start()

# Wyświetlenie grafiki przed modyfikacją
DisplayImageGood()
# Wyświetlenie grafiki po modyfikacji
DisplayImage(receiver.receiverArray)


