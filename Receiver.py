import random
import numpy
import Interference as Interfe
import zlib

class Receiver:
    chosenSumAlgorithm = None
    receivedArray = []
    receivedData = []
    sending = []
    numberOfFrames = 0
    frameSize = 0
    numberOfValues = 0
    xd = 0
    numberOfPositiveSent = 0
    numberOfNegativeSent = 0
    numberOfAllSent = 0

    def __init__(self):
        pass

    def reset_Data(self):
        for i in range(0, self.numberOfFrames):
            self.receivedData.append(0)

    def set_sender(self, sender):
        self.sender = sender
        pass

    def receiver_frame(self):
        for i in range(0, len(self.receivedData)):
            for j in range(0, (len(self.receivedData[i]) - 1)):
                self.receivedArray.append(self.receivedData[i][j])
        self.receivedArray = (numpy.asarray(self.receivedArray)).astype(numpy.uint8)
        print(f'liczba wszystkich przeslanych pakietow: {self.numberOfAllSent}')
        print(f'liczba pozytywnie przeslanych pakietow: {self.numberOfPositiveSent}')
        print(f'liczba ponownie przeslanych pakietow: {self.numberOfNegativeSent}')


    def recieve_frame(self, frame, sequence_number):
        # zaklocenie ramki jesli wylosuje odp warttosc
        rand = random.randrange(0, 100)
        if rand > 90:
            frame = Interfe.interfere_frame(frame,self.frameSize)
        if self.chosenSumAlgorithm == 1:
            checksum = self.count_sum_by_Luhn(frame=frame)
        if self.chosenSumAlgorithm == 2:
            checksum = self.count_sum_by_CRC(frame=frame)
        if self.chosenSumAlgorithm == 3:
            checksum = self.count_parity_bit(frame=frame)

        if checksum == frame[len(frame) - 1]:
            isGood = True
        else:
            isGood = False
        self.numberOfAllSent +=1
        #potwierdzenie poprawnego odbioru lub prosba o ponowne przeslanie
        if isGood:
            # zakłócenie potwierdzenia odbioru
            randix = random.randrange(0, 100)
            if randix > 90:
                print(f'RECEIVER: Wysyłanie powiadomienia ponownego nadesłania pakietu nr "{sequence_number}"')
                self.numberOfNegativeSent += 1
                return False
            else:
                print(f'RECEIVER:odebrano ramkę nr "{sequence_number}"')
                self.receivedData[sequence_number] = frame
                self.numberOfPositiveSent += 1
                return True
        else:
            randix = random.randrange(0, 100)
            if randix < 90:
                print(f'RECEIVER: Wysyłanie powiadomienia ponownego nadesłania pakietu nr "{sequence_number}"')
                self.numberOfNegativeSent += 1
                return False
            else:
                print(f'RECEIVER:odebrano ramkę nr "{sequence_number}"')
                self.receivedData[sequence_number] = frame
                self.numberOfPositiveSent += 1
                return True


    def receive_data_go_back_n(self):
        last_good_frame = -1
        last_sequence_number = -1
        checksum = None
        while last_good_frame < self.numberOfFrames:
            is_frame_good = False
            frame = self.sending[last_good_frame + 1]
            received_sequence_number = self.senfingSEQ[last_good_frame + 1]

            # zakłócenie ramki jeśli wylosuje odp wartość
            rand = random.randrange(0, 100)
            if rand > 90:
                frame = self.interfere(frame)

            if self.chosenSumAlgorithm == 1:
                checksum = self.count_sum_by_Luhn(frame=frame)
            if self.chosenSumAlgorithm == 2:
                checksum = self.count_sum_by_CRC(frame=frame)
            if self.chosenSumAlgorithm == 3:
                checksum = self.count_parity_bit(frame=frame)

            if checksum == frame[len(frame) - 1]:
                is_frame_good = True
            else:
                is_frame_good = False

            if is_frame_good and last_sequence_number + 1 == received_sequence_number:
                # time.sleep(2)
                # zakłócenie potwierdzenia odbioru
                randix = random.randrange(0, 100)
                if randix > 90:
                    self.sender.ACK[last_good_frame + 1] = False
                else:
                    print("received pocket = " + str(last_sequence_number + 1))
                    self.receivedData[last_sequence_number + 1] = frame
                    self.sender.ACK[last_good_frame + 1] = True
                    last_good_frame += 1
                    last_sequence_number += 1
            else:
                # time.sleep(0.2)
                print("you need to resend pocket = " + str(last_sequence_number + 1))
                self.sender.ACK[last_good_frame + 1] = False

        # Metoda odbierająca dla protokołu stop-and-wait

    def receive_frame_stop_and_wait(self, frame, sequenceNumber):
        receivedFrameLength = len(frame)
        checksum = None
        # Otrzymana suma kontrolna

        receivedSum = frame[receivedFrameLength - 1]

        # zaklocenie ramki jesli wylosuje odp warttosc
        rand = random.randrange(0, 100)
        if rand > 90:
            frame = Interfe.interfere_frame(frame)

        if self.chosenSumAlgorithm == 1:
            checksum = self.count_sum_by_Luhn(frame=frame)
        if self.chosenSumAlgorithm == 2:
            checksum = self.count_sum_by_CRC(frame=frame)
        if self.chosenSumAlgorithm == 3:
            checksum = self.count_parity_bit(frame=frame)

        if checksum == receivedSum:
            randix = random.randrange(0, 100)
            if randix < 90:
                self.receivedData[sequenceNumber] = frame
                return True
            else:
                return False
        else:
            randix = random.randrange(0, 100)
            if randix < 90:
                return False
            else:
                self.receivedData[sequenceNumber] = frame
                return True

    def count_sum_by_Luhn(self, frame):
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

    def count_sum_by_CRC(self, frame):
        text = ''
        for i in range(0, len(frame) - 1):
            text += str(frame[i])
        crchex = hex(zlib.crc32(bytes(text, 'utf-8')))
        return crchex


    def count_parity_bit(self, frame):
        count_1 = 0
        for i in range(0, len(frame) - 1):
            helper = frame[i]
            while helper > 0:
                pom = helper % 2
                helper = int(helper / 2)
                if pom == 1:
                    count_1 += 1
        if count_1 % 2 == 1:
            return 1
        else:
            return 0
