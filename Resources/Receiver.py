class Receiver:
    receivedArray = None

    def __init__(self):
        pass

    def set_sender(self, sender):
        self.sender = sender
        pass

    def receiver_frame(self, frame):
        self.receivedArray = frame
        pass

    pass
