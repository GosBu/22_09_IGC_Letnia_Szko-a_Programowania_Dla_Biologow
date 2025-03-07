# OB2 Stwórz kilka instancji klasy Osoba, zmień imię na pusty ciąg znaków

class Osoba:


    def __init__(self, imie, nazwisko, wiek, kolor_oczu, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kolor_oczu = kolor_oczu
        self.plec = plec
        self.narodowsoc = narodowosc = 'Polak'

# instancje

osoba_1 = Osoba('Anna', 'Zwierz', 32, 'niebieski', 'kobieta')
osoba_2 = Osoba('Marian', 'Nowak', 2, 'brązowy', 'mezczyzna')
osoba_3 = Osoba('Tomasz', 'Drzwi', 15, 'niebieski', 'mezczyzna')
print(osoba_1, osoba_2, osoba_3)

osoba_1.imie = ' '        #niedokończone zadanie!
