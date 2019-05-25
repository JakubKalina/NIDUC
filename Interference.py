import random

# procent zakłóceń; mniejszy procent to mniej zakłóceń
interference_ratio = 0.01


# zakłóć tablice
def interfere(array):

    # ilość zakłóconych wartości
    count = int(array.size * interference_ratio)

    for i in range(0, count):
        # losujemy indeks do zakłócenia
        index_to_interfere = random.randint(0, array.size)

        # zakłócamy wybraną wartość
        array[index_to_interfere] = random.randint(0, 256)

        pass
    return array
