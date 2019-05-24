from abc import ABC, abstractmethod
from Resources.Sender import Sender
from Resources.Receiver import Receiver


class Protocol(ABC):

    def __init__(self, sender, receiver):
        if not isinstance(sender, Sender):
            raise TypeError('Pole "sender" musi być typu "Sender"!')

        if not isinstance(receiver, Receiver):
            raise TypeError('Pole "receiver" musi być typu "Receiver"!')

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
