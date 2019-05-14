import time
class GoBackNSender:

    windowSize = 10
    timeout = 0.5
    receivedACK = []

    def __init__(self, windowSize, timeout, receiver):
        self.windowSize = windowSize
        self.timeout = timeout
        self.receiver = receiver
        self.receiver.senderACK = self.receivedACK
        pass


    def sendframe(self, frame):
        firstPoint = 0

        # podziel przez ilosc pol w rgba
        end = int(frame.size / 4)

        # wykonuj do długosci ramki
        while firstPoint < end:

            # Sprawdz czy okno nie wykracza poza zakres
            if (firstPoint + self.windowSize) >= end:
                lastPoint = end
            else:
                lastPoint = firstPoint + self.windowSize

            # wyslij wszyskie plik w danym oknie
            for index in range(firstPoint, lastPoint):

                # wysyłanie obiektu z ramki
                self.receiver.receiveobject(frame[index]);
                pass

            # sprawdz otrzymane ATK
            for index in range(firstPoint, lastPoint):
                # Czekaj na otrzymanie obiektu
                time.sleep(self.timeout)
                # Dopóki nie otrzymano atk wysylaj plik
                while self.receivedACK[index] == False:
                    self.receiver.receiveobject(frame[index], index)
                    time.sleep(self.timeout)
                    pass
                pass

            # inkrementuj tablice
            firstPoint =+ lastPoint
            pass
        return frame

    pass

class GoBackNReceiver:

    frameReceived = []
    indexOfFrame = 0
    senderACK = []

    def __init__(self, windowSize, timeout):
        self.windowSize = windowSize
        self.timeout = timeout
        self.sender = GoBackNSender(windowSize=self.windowSize,timeout=self.timeout,receiver=self)
        pass

    # odbieranie jednego piksela z ramki
    def receiveobject(self,object):
        # sprawdz czy nie jest uszkodzony
        if object is not None:
            # zaakceptuj plik
            self.frameReceived.append(object)
            self.sender.receivedACK.append(True)
        else:
            self.sender.receivedACK.append(False)

        # ustaw ACK
        self.sender.receivedACK = self.senderACK

        # timeout
        time.sleep(self.timeout)
    pass

    # Popraw uszkodzone pliki
    def receiverobject(self, object, index):
        if index < self.frameReceived.size and index > 0 and object is not None:
            self.frameReceived[index] = object

        # zmien ATK po poprawieniu obiektu
        self.sender.receivedACK[index] = True
        pass

    # pobierz Ramke
    def getFrame(self, frame):
        # odbierz przeslana ramke
        receivedFrame = self.sender.sendframe(frame)
        return receivedFrame