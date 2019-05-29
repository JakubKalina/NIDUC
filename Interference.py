import random

# procent zakłóceń; mniejszy procent to mniej zakłóceń
interference_ratio = 0.99


# zakłóć tablice
def interfere(array):

    # ilość zakłóconych wartości
    count = int(array.size * interference_ratio)

    for i in range(0, count):
        # losujemy indeks do zakłócenia
        index_to_interfere = random.randint(0, array.size -1)

        # zakłócamy wybraną wartość
        array[index_to_interfere] = random.randint(0, 256)
        pass
    return array

def interfere_frame(frame, sizeOfFrame):
    table = []
    for i in range(0, sizeOfFrame):
        table.append(random.randint(0, 256))
    table.append(int(frame[(len(frame) - 1)]))
    return table
