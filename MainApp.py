from tkinter import *
from Sender import Sender
from Receiver import Receiver
from PIL import ImageTk, Image

# Funkcja wyświetlająca obraz
def DisplayImage(receivedArray):
    img = Image.fromarray(receivedArray)
    img.save('test.png')
    window = Tk()
    img = ImageTk.PhotoImage(Image.open("test.png"))
    panel = Label(window, image=img)
    panel.pack()
    window.mainloop()


# Obiekt nadajnika
sender = Sender()

# Obiekt odbiornika
receiver = Receiver()

# Załadowanie obrazu z pliku do tablicy
sender.LoadImage()


index = 0
while index < 64:
    frame = sender.SendFrame(index)

    for i in range(0,64):
        for j in range(0,3):
            frame[i][j] = 0

    receiver.receiveImage(frame, index)
    #print(receiver.frame)
    #print('\n')
    index = index + 1


# Wyświetlenie grafiki przed modyfikacją
DisplayImage(sender.senderArray)
# Wyświetlenie grafiki po modyfikacji
DisplayImage(receiver.receiverArray)


