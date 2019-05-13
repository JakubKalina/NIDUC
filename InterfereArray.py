import random

class InterfereArray:

    # Metoda przyjmująca niezakłóconą tablicę
    def Interfere(self, arrayToInterfere, height, width):

        index = 0;

        for i in range(0,height):
            for j in range(0, width):
                for k in range(0,3):
                    randomNumber = random.randint(1,10)
                    if randomNumber == 1:
                        arrayToInterfere[i][j][k] = 0

        # Zwrócenie zakłóconej tablicy
        return arrayToInterfere