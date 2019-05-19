from .Protocol import Protocol

class StopAndWait(Protocol):

    def sender_end_point(self, array):
        print("Welcome to the sender")
        pass

    def receiver_end_point(self, array):
        print("Welcome to the receiver")
        pass

    def start_transmission(self):
        print("Welcome to the start transmission")
        pass

    pass
