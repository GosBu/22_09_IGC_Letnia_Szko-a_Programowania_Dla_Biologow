# Stwórz trzy pliki
# W pierwszym ma być klasa Osoba
# W drugim klasą ma być Adres
# W trzeci pliku (start.py) chcemy je zaimportować i utworzyć osobę o konkretnym adresie

# PLIK pierwszy

class Osoba:
    def __init__(self, imie, nazwisko, wiek, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.adres = adres

    def __str__(self):
        return f'[Osoba]{self.imie}, {self.nazwisko}, {self.wiek}, {self.adres}'

osoba_1 = Osoba('Paweł', 'Kowalski', 18, 'Poznań')
print(osoba_1)
