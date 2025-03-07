# FU7 Stwórz funkcję, która po każdym wywołaniu zmodyfikuje zmienną globalną o nazwie licznik
# (doda 1)

licznik = 10


def modyfikacja_licznika():
    global licznik
    licznik += 1
    print(licznik)

modyfikacja_licznika()
