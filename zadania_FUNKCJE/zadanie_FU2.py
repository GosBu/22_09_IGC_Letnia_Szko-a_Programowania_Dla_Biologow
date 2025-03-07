# FU2 Stwórz funkcję, która dla zadanej listy wartości liczbowych będzie liczyła ich sumę
# średnią, medianę, odchylenie standardowe
# i zwróci te wartości w postaci krotki

from statistics import mean, median, stdev

moja_lista = [1, 45, 16, 12, 234, 50]


def moja_funkcja(liczby):
    return mean(liczby), sum(liczby), stdev(liczby)


print(moja_funkcja(moja_lista))
