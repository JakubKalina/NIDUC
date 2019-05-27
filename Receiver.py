import random
import time
import Interference as interfere
import numpy


class Receiver:
    receivedArray = []
    receivedData = []
    sending = []
    numberOfFrames = 0
    frameSize = 0
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
        print(self.receivedData)
        for i in range(0, len(self.receivedData)):
            for j in range(0, (len(self.receivedData[i]) - 1)):
                self.receivedArray.append(self.receivedData[i][j])
        print(self.receivedArray)

    def recieve_frame(self, frame, sequence_number):
        isGood = False

        # zaklocenie ramki jesli wylosuje odp warttosc
        rand = random.randrange(0, 100)
        if rand > 99:
            frame = self.interfere(frame)
        checksum = self.count_sum(frame=frame)
        if checksum == frame[len(frame) - 1]:
            isGood = True
        else:
            isGood = False

        if isGood:
            # time.sleep(2)
            # zakłócenie potwierdzenia odbioru
            randix = random.randrange(0, 100)
            if randix > 90:
                return False
            else:
                print(f'RECEIVER:odebrano ramkę nr "{sequence_number}"')
                self.receivedData[sequence_number] = frame
                return True
        else:
            # time.sleep(0.2)
            print(f'RECEIVER: Wysyłanie powiadomienia ponownego nadesłania pakietu nr "{sequence_number}"')
            return False;

    def receive_data_go_back_n(self):
        last_good_frame = -1
        last_sequence_number = -1

        while last_good_frame < self.numberOfFrames:
            is_frame_good = False
            frame = self.sending[last_good_frame+1]
            received_sequence_number = self.senfingSEQ[last_good_frame+1]

            # zakłócenie ramki jeśli wylosuje odp wartość
            rand = random.randrange(0, 100)
            if rand > 90:
                frame = self.interfere(frame)
            checksum = self.count_sum(frame)

            if checksum == frame[len(frame) - 1]:
                is_frame_good = True
            else:
                is_frame_good = False

            if is_frame_good and last_sequence_number+1 == received_sequence_number:
                # time.sleep(2)
                # zakłócenie potwierdzenia odbioru
                randix = random.randrange(0, 100)
                if randix > 90:
                    self.sender.ACK[last_good_frame+1] = False
                else:
                    print("received pocket = " + str(last_sequence_number+1))
                    self.receivedData[last_sequence_number+1] = frame
                    self.sender.ACK[last_good_frame+1] = True
                    last_good_frame += 1
                    last_sequence_number += 1
            else:
                # time.sleep(0.2)
                print("you need to resend pocket = " + str(last_sequence_number+1))
                self.sender.ACK[last_good_frame + 1] = False

        # Metoda odbierająca dla protokołu stop-and-wait
    def receive_frame_stop_and_wait(self, frame, sequenceNumber):
        receivedFrameLength = len(frame)
        # Otrzymana suma kontrolna
        receivedSum = frame[receivedFrameLength - 1]

        # zaklocenie ramki jesli wylosuje odp warttosc
        rand = random.randrange(0, 100)
        if rand > 90:
            frame = self.interfere(frame)
        checksum = self.count_sum(frame)

        if checksum == receivedSum:
            self.receivedData[sequenceNumber] = frame
            return True
        else:
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
        table = []
        for i in range(0, len(frame) - 1):
            table.append(random.randint(0, 256))
        table.append(int(frame[(len(frame) - 1)]))
        return table


