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
        number =0
        while counter < len(self.image) -1:
            if(b < self.size):
                row.append(self.image[counter])
                b = b+1
                counter += 1
                number+=1
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


        Receiver.sizeOfTableFrames = sizeoftable
        Receiver.sizeFrame = number
        i = 0
        while i < sizeoftable:
            #if self.ACK[i] == False:
                Receiver.receivedData.append(self.tableOfFrames[i])
                i+=1


