from .Protocol import Protocol
from ..Interference import interfere_frame
import threading
import time
import numpy


class GoBackN(Protocol, threading.Thread):
    sender_timeout = 0.1
    receiver_timeout = 0.1
    exit_loop = True
    delay = 0.01

    def __init__(self, sender, receiver, window_size, array_size):
        threading.Thread.__init__(self)
        super().__init__(sender=sender, receiver=receiver)

        self.object_size = array_size

        if window_size > 0:
            self.window_size = window_size
        else:
            window_size = array_size / 5 + 1
        self.sender = sender
        self.receiver = receiver

        frame = Frame()
        frame.seq_number = -1
        frame.value = -1
        self.coming_data = numpy.full((self.object_size), frame)
        self.received_data = numpy.full((self.object_size), frame)
        self.ACK = numpy.full((self.object_size), False)
        pass

    def sender_end_point(self, array):
        i = 0
        win_start = i
        win_end = i + self.window_size
        while i < array.size:
            while i < win_end and i < array.size:
                frame = Frame()
                frame.value = array[i]
                frame.seq_number = i

                # wysyłanie
                #                if i == 5:
                #                   time.sleep(10)

                self.coming_data[i] = frame

                print(f'SENDER: wysłano obiekt nr "{i}" \n')
                time.sleep(self.delay)
                if self.ACK[win_start]:
                    print(f'SENDER: odebrano\n')
                    win_end += 1
                    win_start += 1
                    # i = win_start

                i += 1
                time.sleep(self.delay)
                pass
            pass
            time.sleep(self.sender_timeout)
            if i == win_end:
                i = win_start
            pass

        print('SENDER: koniec wysyłania\n')
        pass

    def receiver_end_point(self, expected_length):
        last_seq_number = -1
        i = 0
        while i < expected_length:
            time.sleep(self.delay/2)

            if i == 0 and self.coming_data[0].value == -1 and self.coming_data[0].seq_number == -1:
                print("Czekam na rozpoczęcie przesyłania danych\n")
                time.sleep(self.receiver_timeout)
                continue

            frame = self.coming_data[i]

            if frame.seq_number == -1:
                print('RECEIVER: nie wysłano ramki, wysyłam powiadomienie\n')
                time.sleep(self.delay)
                continue

            # Kiedy numer sekwencyjny jest losowy pakiet nie zostanie przyjety
            #            if i == 5:
            #                frame = interfere_frame(frame)

            if frame.seq_number != last_seq_number + 1:
                time.sleep(self.delay)
                print(f'RECEIVER: Bład. Ma być {last_seq_number + 1} a jest {frame.seq_number}')
                self.ACK[last_seq_number + 1] = False
                continue
            else:
                time.sleep(self.delay)
                print(f'RECEIVER: nadesłano poprawny pakiet nr [{frame.seq_number}]')
                self.ACK[frame.seq_number] = True
                self.received_data[frame.seq_number] = frame.value
                last_seq_number += 1
                i += 1

        print('RECEIVER: Odebrano zamierzone pliki')
        self.exit_loop = False
        pass

    def start_transmission(self, array):
        print("Welcome to the start transmission\n")
        threading.Thread(target=self.sender_end_point, args=(array,)).start()
        threading.Thread(target=self.receiver_end_point, args=(len(array),)).start()

        while (self.exit_loop):
            time.sleep(0.5)
            pass
        pass

    pass


class Frame:
    value = 0
    seq_number = 0
    pass
