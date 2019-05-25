
class Receiver:
    receivedArray = []
    receivedData = []
    sizeOfTableFrames = 0
    sizeFrame = 0

    def __init__(self):
        pass

    def set_sender(self, sender):
        self.sender = sender
        pass

    def receiver_frame(self):
        print (self.receivedData)
        p = 0

        #while p < self.sizeOfTableFrames:




        for i in range (0, len(self.receivedData)):
            for j in range (0, len(self.receivedData[i])):
                self.receivedArray.append(self.receivedData[i][j])
        print(self.receivedArray)

