# FU1 Stwórz funkcję, która będzie przyjmowała wartości imię nazwisko i wiek,
# gdzie wiek będzie miał wartość domyślną 3 i wypisze je na ekranie


def moja_funkcja(imie, nazwisko, wiek=3):
    print(imie, nazwisko, wiek)
moja_funkcja('gosia', 'bujak', 31)

# 1)


def moja_funkcja(imie, nazwisko, wiek=3):
    print(imie, nazwisko, wiek)


moja_funkcja('Gosia', 'Bujak', 31)

# 2)
dane = {'imie': 'Waldemar', 'nazwisko': 'Nowak', 'wiek': 23}


def moja_funkcja(imie, nazwisko, wiek=3):
    print(imie, nazwisko, wiek)


moja_funkcja(** dane)
