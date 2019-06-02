import random

def interfere_frame(frame, sizeOfFrame):
    table = []
    for i in range(0, sizeOfFrame):
        table.append(random.randint(0, 256))
    table.append(int(frame[(len(frame) - 2)]))
    return table
