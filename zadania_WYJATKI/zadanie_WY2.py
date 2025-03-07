# WY2 Zmodyfikuj Osobę z zadania OB5 tak że próba ustawienia pustego imienia będzie zgłaszała
# wyjątek.

class Osoba:


    def __init__(self, imie, nazwisko, wiek, kolor_oczu, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kolor_oczu = kolor_oczu
        self.plec = plec

    def __str__(self):
        print(f'Osoba{osoba_1}')

# NIE ZROBIONE
