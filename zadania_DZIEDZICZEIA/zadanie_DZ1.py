# DZ1 Stwórz klasę Uczen oraz klasę Nauczyciel rozszerzające klasę Osoba. Uczeń powinien miećro

from statistics import mean

class Osoba:


    def __init__(self, imie, nazwisko, wiek):
        self.__imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek


class Uczen(Osoba):

    def __init__(self, imie, nazwisko, wiek):
        super().__init__(self, imie, nazwisko, wiek)
        self.dzienniczek = []

    def dodaj_ocene(self, ocena):
        self.dzienniczek.append(ocena)

    def srednia_ocen(self):
        # self.srednia_ocen = sum(self.dzienniczek) / len(self.dzienniczek)
        return mean(self.dzienniczek)

class Nauczyciel(Osoba):

    def __init__(self, imie, nazwisko, wiek, uczniowie):
        super().__init__(self, imie, nazwisko, wiek, uczniowie)
        self.lista_uczniow = []

    def dodaj_ucznia(self, uczniowie):
        self.lista_uczniow.append(uczniowie)

    def __str__(self):
        return f'[Nauczyciel] {self.imie}, {self.nazwisko}, {self.wiek}, {self.lista_uczniow}'

uczen_1 = Uczen('Jan', 'Nowak', 12)
print(uczen_1)
uczen_1.dodaj_ocene(4)
print(uczen_1.srednia_ocen())
