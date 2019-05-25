from Receiver import Receiver
import time


class Sender:
    ACK = []
    size = None
    windowSize = None
    tableOfFrames = []

    def __init__(self, receiver):
        self.receiver = receiver
        pass

    def send_frame(self, frame):
        self.receiver.receiver_frame(frame)
        pass

    def send_frame_selective(self):
        i = 0;
        counter = 0
        b = 0
        row = []
        number = 0

        # dzieli obraz na ramki gotowe do przeslania
        while counter < len(self.image) - 1:
            if (b < self.size):
                number += 1
                row.append(self.image[counter])
                b = b + 1
                counter += 1
            else:
                #generowanie sumy kontrolnej algorytmem Luhna
                sum = 0
                for k in range (0, len(row)):
                    help = row[k]
                    while help > 0:
                        sum += help%10
                        help = int(help/10)
                sum = sum%10
                sum = 10 - sum
                row.append(sum)
                self.tableOfFrames.append(row)
                row = []
                b = 0
            if counter == len(self.image) - 1:
                sum = 0
                for k in range(0, len(row)):
                    help = row[k]
                    while help > 0:
                        sum += help%10
                        help = int(help/10)
                sum = sum % 10
                sum = 10 - sum
                row.append(sum)
                self.tableOfFrames.append(row)
                counter += 1

        #drukuje wszystkie ramki
        print(self.tableOfFrames)

        #pokazuje ilosc ramek
        sizeoftable = len(self.tableOfFrames)

        #tworzy tablice o rozmiarze ilosci ramek z potwierdzeniami lub odrzuceniami pakietów
        for i in range(0, sizeoftable):
            self.ACK.append(False)

        #przenoszenie do receivera potrzebnych wartosci
        Receiver.numberOfValues = number
        Receiver.numberOfFrames = sizeoftable
        Receiver.reset_Data(Receiver)
        i=0
        endOfWindow = self.windowSize -1

        #petla wysylajaca ramki zgodnie z regulami algotrytmu selektywnego
        while i < sizeoftable:
            isCorrectFrame = True
            #petla operujaca oknem i wysylajaca te ramki ktore sender od nas chce
            for j in range (i , endOfWindow + 1):
                if j == sizeoftable:
                    break
                if self.ACK[j] == False:
                    time.sleep(0.2)
                    print("Sending pocket = " + str(j))
                    self.ACK[j] = Receiver.recieve_frame(Receiver, self.tableOfFrames[j], j)
                else:
                    pass
            #petla sprawdzajaca czy cala ramka zostala przeslana bez zarzutów
            for j in range(i, endOfWindow + 1):
                if j == sizeoftable:
                    break
                if self.ACK[j] == False:
                    isCorrectFrame = False
            #warunki odpowiadajace za przesuwanie sie okna gdy ramka jest dobra lub gdy ktorys z pakietow jest uszkodzony
            if isCorrectFrame:
                if (endOfWindow + self.windowSize) >= sizeoftable:
                    endOfWindow = sizeoftable
                else:
                    endOfWindow += self.windowSize
                i += self.windowSize
            else:
                count = 0
                for j in range(i, endOfWindow + 1):
                    if self.ACK[j] == True:
                        count += 1
                    else:
                        break
                endOfWindow += count
                i += count


