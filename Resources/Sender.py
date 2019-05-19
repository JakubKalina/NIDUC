from Resources.protocols.Protocol import Protocol


class Sender:

    def __init__(self, protocol):
        if not isinstance(protocol, Protocol):
            raise TypeError('Pole \'protocol\' musi być typu \'Protocol\'!')
        self.protocol = protocol
        pass
    pass
