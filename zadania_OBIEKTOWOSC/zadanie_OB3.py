# OB3 Zmodyfikuj klasę Osoba tak, żeby dodać funkcje dostępowe a atrybuty ustawić na prywatne
class Osoba:

    def __init__(self, imie, nazwisko, wiek, kolor_oczu, plec):
        self.__imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kolor_oczu = kolor_oczu
        self.plec = plec

    def __str__(self):
        return f'Osoba {self.__imie} {self.nazwisko} {self.wiek} {self.kolor_oczu} {self.plec}'


nowa_osoba = Osoba('Kasia', 'Kowalska', 30, 'zielony', 'kobieta')
print(nowa_osoba)


def __get_imie(self):
    return self.__imie


def __set_imie(self, nowe_imie):
    if nowe_imie != ' ':
        self._imie = nowe_imie
    else:
        self._imie = 'Brak imienia'


osoba_1 = Osoba('Anna', 'Zwierz', 32, 'niebieski', 'kobieta')
osoba_2 = Osoba('Marian', 'Nowak', 2, 'brązowy', 'mezczyzna')
osoba_3 = Osoba('Tomasz', 'Drzwi', 15, 'niebieski', 'mezczyzna')
print(osoba_1, osoba_2, osoba_3)

osoba_1.set_imie('')
print(osoba_1)