from Receiver import Receiver
import time
import Image


class Sender:
    ACK = []
    size = None
    windowSize = None
    tableOfFrames = []
    ChosenSumAlgorithm = None
    def __init__(self, receiver):
        self.receiver = receiver
        pass

    def send_frame(self, frame):
        self.receiver.receiver_frame(frame)
        pass

    def send_frame_selective(self):
        #stworzenie tablicy z ramkami
        self.tableOfFrames = Image.gruop_into_frames(self.image, self.size, self.ChosenSumAlgorithm)

        # zapisuje ilosc ramek dopedli wysylania
        sizeoftable = len(self.tableOfFrames)

        # tworzy tablice o rozmiarze ilosci ramek z potwierdzeniami lub odrzuceniami pakietów
        for i in range(0, sizeoftable):
            self.ACK.append(False)

        # przenoszenie do receivera potrzebnych wartosci
        Receiver.numberOfFrames = sizeoftable
        Receiver.reset_Data(Receiver)
        endOfWindow = self.windowSize - 1
        i = 0
        # petla wysylajaca ramki zgodnie z regulami algotrytmu selektywnego
        while i < sizeoftable:
            isCorrectFrame = True
            # petla operujaca oknem i wysylajaca te ramki ktore sender od nas chce
            for j in range(i, endOfWindow + 1):
                if j == sizeoftable:
                    break
                if self.ACK[j] == False:
                    # time.sleep(0.2)
                    print(f'SENDER: wysłano obiekt nr "{j}"')
                    self.ACK[j] = self.receiver.recieve_frame(self.tableOfFrames[j], j)
                else:
                    pass
            # petla sprawdzajaca czy cala ramka zostala przeslana bez zarzutów
            for j in range(i, endOfWindow + 1):
                if j == sizeoftable:
                    break
                if self.ACK[j] == False:
                    isCorrectFrame = False
            # warunki odpowiadajace za przesuwanie sie okna gdy ramka jest dobra lub gdy ktorys z pakietow jest uszkodzony
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

    def send_frame_go_back_n(self, delay):
        # self.image = interfere(self.image)
        # przygotowanie ramek fo wysłania
        # 1. stworzenie tablicy ramek z sumą kontrolną
        self.tableOfFrames = Image.gruop_into_frames(self.image, self.size, self.ChosenSumAlgorithm)

        # pokazuje ilość ramek
        size_of_table = len(self.tableOfFrames)

        # tworzy tablice o rozmiarze ilości ramek z potwierdzeniami lub odrzuceniami pakietów
        for i in range(0, size_of_table):
            self.ACK.append(False)

        # przenoszenie do receivera potrzebnych wartości
        self.receiver.numberOfValues = self.image.size
        self.receiver.numberOfFrames = len(self.tableOfFrames)
        self.receiver.reset_Data()

        # rozpoczęcie przesyłania
        i = 0
        win_start = i
        win_end = i + self.windowSize
        length_table_of_frames = len(self.tableOfFrames)

        while i < length_table_of_frames:
            while i < win_end and i < length_table_of_frames:
                # pobranie ramki do wysłania
                data = self.tableOfFrames[i]
                sequence_number = i

                # wysyłanie ramki
                print(f'\nSENDER: wysłano obiekt nr "{i}"')
                self.ACK[i] = self.receiver.recieve_frame(frame=data, sequence_number=sequence_number)

                time.sleep(delay)
                if self.ACK[win_start]:
                    print(f'SENDER: odebrano ATK "{win_start}"\n')
                    win_end += 1
                    win_start += 1
                    # i = win_start
                else:
                    if win_end > length_table_of_frames:
                        win_end = length_table_of_frames
                    for k in range(win_start + 1, win_end):
                        if self.ACK[k]:
                            print(f'SENDER: odebrano ATK "{k}, Pominięto ATK "{win_start}"\n')
                            i = win_start - 1
                            break

                i += 1
                time.sleep(delay)
                pass
            pass
            time.sleep(delay)
            if i == win_end:
                i = win_start
            pass

        print('SENDER: koniec wysyłania\n')
        pass

# Metoda wysyłająca dla protokołu stop-and-wait
    def send_frame_stop_and_wait(self):
        # test
        # print(self.image)
        self.tableOfFrames = Image.gruop_into_frames(self.image, self.size, self.ChosenSumAlgorithm)

        #wyświetlenie tablicy zawierającej wszystkie ramki
        print(self.tableOfFrames)

        #zapis ilości ramek
        sizeoftable = len(self.tableOfFrames)

        #tworzy tablice o rozmiarze ilosci ramek z potwierdzeniami lub odrzuceniami pakietów
        for i in range(0, sizeoftable):
            self.ACK.append(False)

        #przenoszenie do receivera potrzebnych wartosci
        Receiver.numberOfValues = number
        Receiver.numberOfFrames = sizeoftable
        Receiver.reset_Data(Receiver)
        i = 0
        endOfWindow = self.windowSize -1

        print("Rozmiar tablicy ramek:")
        print(sizeoftable)

        #wysyłanie poszczególnych ramek
        while i < sizeoftable:
            self.ACK[i] = self.receiver.receive_frame_stop_and_wait(self.tableOfFrames[i], i)
            if self.ACK[i]:
                i += 1
            else:
                self.ACK[i] = False
                continue

class Frame:
    value = None
    seq_number = 0
    pass
