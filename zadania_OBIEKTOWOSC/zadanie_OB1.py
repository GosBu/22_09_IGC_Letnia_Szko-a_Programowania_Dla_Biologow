# OB1 Stwórz klasę Osoba (każda osoba ma imię, nazwisko, wiek)

class Osoba:


    def __init__(self, imie, nazwisko, wiek, kolor_oczu, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kolor_oczu = kolor_oczu
        self.plec = plec
        self.narodowsoc = narodowosc = 'Polak'

    def __str__(self):
        return f'Osoba {self.imie} {self.nazwisko} {self.wiek} {self.kolor_oczu} {self.plec}'

nowa_osoba = Osoba('Kasia', 'Kowalska', 30, 'zielony', 'kobieta')
print(nowa_osoba)
