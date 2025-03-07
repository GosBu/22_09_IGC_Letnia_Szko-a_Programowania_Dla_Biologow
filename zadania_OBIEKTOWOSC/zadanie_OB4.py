# OB4 Zmodyfikuj klasę Osoba tak żeby wykorzystać właściwości do ustalania oraz zmiany
# atrybutów

class Osoba:


    def __init__(self, imie, nazwisko, wiek, kolor_oczu, plec):
        self.__imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kolor_oczu = kolor_oczu
        self.plec = plec

# instancje

osoba_1 = Osoba('Anna', 'Zwierz', 32, 'niebieski', 'kobieta')
osoba_2 = Osoba('Marian', 'Nowak', 2, 'brązowy', 'mezczyzna')
osoba_3 = Osoba('Tomasz', 'Drzwi', 15, 'niebieski', 'mezczyzna')
print(osoba_1, osoba_2, osoba_3)

def __get_imie(self):
    return self.__imie


def __set_imie(self, nowe_imie):
    self.__imie =