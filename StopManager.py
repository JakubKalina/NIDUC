from tkinter import *
from PIL import ImageTk, Image
import numpy as np

class StopManager:


    # Protokół stop-and-wait
    def StopAndWaitProtocol(self, sender, receiver, height ):

        # Indeks pętli
        index = 0

        # Do czasu aż przesłano wszystkie ramki z informacjami
        while index < height:

            # Wysyłana ramka
            frame = sender.SendFrame(index)

            # Suma kontrolna wysyłanej ramki
            sumBefore = sender.GenerateControlSum(index)


            # Tutaj zakłucenie danych / tablicy !!!

            # Sprawdzenie czy suma kontrolna się zgadza
            isCorrect = receiver.receiveImage(frame, index, sumBefore)

            # Jeśli suma kontrolna jest niezgodna to wyślij ponownie
            if isCorrect == False:
                continue;
            else:
                index = index + 1

        # Zwrócenie uzyskanej tablicy z danymi do wyświetlenia
        return receiver.receiverArray

