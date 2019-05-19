from abc import ABC, abstractmethod
import threading


class Protocol(ABC, threading.Thread):
    Sender = None
    Receiver = None

    def __init__(self, sender, receiver):
        self.Sender = sender
        self.Receiver = receiver
        pass

    @abstractmethod
    def sender_end_point(self):
        pass

    @abstractmethod
    def receiver_end_point(self):
        pass

    @abstractmethod
    def start_transmission(self):
        pass

    pass
