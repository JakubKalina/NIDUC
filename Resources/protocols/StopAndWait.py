from .Protocol import Protocol
import threading


class StopAndWait(Protocol):

    def __init__(self, sender, receiver):
        super().__init__(sender=sender, receiver=receiver)
        self.sender = sender
        self.receiver = receiver
        pass

    def sender_end_point(self, array):
        print("Welcome to the sender")
        self.sender.send_frame(array)
        pass

    def receiver_end_point(self, array):
        print("Welcome to the receiver")
        pass

    def start_transmission(self, array):
        print("Welcome to the start transmission")
        threading.Thread(target=self.sender_end_point(array)).start()
        threading.Thread(target=self.receiver_end_point(array)).start()
        pass

    pass
