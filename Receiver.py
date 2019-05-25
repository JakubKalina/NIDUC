
class Receiver:
    receivedArray = []
    receivedData = []
    numberOfFrames = 0
    frameSize = 0;
    numberOfValues = 0

    def __init__(self):
        pass

    def reset_Data(self):
        for i in range(0, self.numberOfFrames):
            self.receivedData.append(0)

    def set_sender(self, sender):
        self.sender = sender
        pass

    def receiver_frame(self):
        print (self.receivedData)

        for i in range (0, len(self.receivedData)):
            for j in range (0, len(self.receivedData[i])):
                self.receivedArray.append(self.receivedData[i][j])
        print(self.receivedArray)



    def recieve_frame(self, frame, sequence_number):

        #tutaj sprawdza czy suma kontrolna jest OK
        isGood = True

        if (isGood):
            #self.receivedData.append(frame)
            self.receivedData[sequence_number] = frame
            return True;
        else:
            return False
