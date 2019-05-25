import random
import time
import Interference as interfere

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
        rand = random.randrange(0, 100)
        #zepsucie obrazu jesli wylosuje wartosc

            #zostanie dodane jutro



        sumi = self.count_sum(self, frame)


        if sumi == frame[len(frame) - 1]:
            isGood = True
        else:
            isGood = False




        if (isGood):
            time.sleep(0.2)
            print("received pocket = " + str(sequence_number))
            self.receivedData[sequence_number] = frame
            return True;

        else:
            time.sleep(0.2)
            print("you need to resend pocket = " + str(sequence_number))
            return False



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
        for i in range(0, len(frame)):
            frame = random.randint(0, 255)
            pass
        return frame
