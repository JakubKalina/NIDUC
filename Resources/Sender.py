
class Sender:

    def __init__(self, receiver):
        self.receiver = receiver
        pass

    def send_frame(self, frame):
        self.receiver.receiver_frame(frame)
        pass
