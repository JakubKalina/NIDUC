from Receiver import Receiver
import time 

class Sender:
    ACK = []
    NAQ = []
    size = None
    windowSize = None
    tableOfFrames =[]

    def __init__(self, receiver):
        self.receiver = receiver
        pass

    def send_frame(self, frame):
        self.receiver.receiver_frame(frame)
        pass
    
    def send_frame_selective (self):
        i=0;
        counter = 0
        b = 0
        row = []
        number = 0
        while counter < len(self.image) -1:
            if(b < self.size):
                number += 1
                row.append(self.image[counter])
                b = b+1
                counter += 1
            else:
                self.tableOfFrames.append(row)
                row = []
                b=0
            if counter == len(self.image) -1:
                self.tableOfFrames.append(row)
                counter +=1
        print(self.tableOfFrames)
        sizeoftable = len(self.tableOfFrames)
        for i in range(0,sizeoftable):
            self.ACK.append(False)

        i = 0
        Receiver.numberOfValues = number
        Receiver.numberOfFrames = sizeoftable
        Receiver.reset_Data(Receiver)
        while i < sizeoftable:
            #Receiver.receivedData.append(self.tableOfFrames[i])
            self.ACK[i] = Receiver.recieve_frame(Receiver, self.tableOfFrames[i], i)

            if(self.ACK[i]):
                i += 1
            else:
                continue


