import random
import time
import Interference as interfere
import numpy

class Receiver:
    receivedArray = []
    receivedData = []
    numberOfFrames = 0
    frameSize = 0;
    numberOfValues = 0
    xd = 0

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
            for j in range (0, (len(self.receivedData[i]) - 1)):
                self.receivedArray.append(self.receivedData[i][j])
        print(self.receivedArray)


    def recieve_frame(self, frame, sequence_number):
        isGood = False
        #zaklocenie ramki jesli wylosuje odp warttosc
        rand = random.randrange(0, 100)
        if rand > 90:
            frame = self.interfere(self, frame)
        checksum = self.count_sum(self, frame)
        if checksum == frame[len(frame) - 1]:
            isGood = True
        else:
            isGood = False

        if (isGood):
            #time.sleep(0.2)
            #zaklocenie potwierdzenia odbioru
            randix = random.randrange(0, 100)
            if randix > 90:
                return False;
            else:
                print("received pocket = " + str(sequence_number))
                self.receivedData[sequence_number] = frame
                return True
        else:
            #time.sleep(0.2)
            print("you need to resend pocket = " + str(sequence_number))
            return False;


    def count_sum(self, frame):
        sum = 0
        for k in range(0, len(frame) - 1):
            help = frame[k]
            while help > 0:
                sum += help % 10
                help = int(help / 10)
                pass
        sum = sum % 10
        sum = 10 - sum
        return sum


    def interfere(self, frame):
        table = []
        for i in range(0, len(frame) -1 ):
            table.append(random.randint(0, 256))
        table.append(int(frame[(len(frame) - 1)]))
        return table
