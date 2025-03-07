# FU3 Stwórz funkcję, która przyjmie, jako argument listę osób (z zadania SL2) a następnie zwróci
# osoby pełnoletnie

moj_slownik = [{'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 1, 'adres': 'Al.Krakwoskie 15', 'wzrost': '176'},
               {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Al.Ujazdowskie 10', 'wzrost':'160'},
               {'imie': 'Aldona', 'nazwisko': 'Buczkowska', 'wiek': 40, 'adres': 'ul. Powstancow Wielkopolsich 12/1', 'wzrost':180},
               {'imie': 'Dorota', 'nazwisko': 'Poniatowska', 'wiek': 20, 'adres': 'os. Batorego 12/150', 'wzrost':168},
               {'imie': 'Basia', 'nazwisko': 'Nowacka', 'wiek': 5, 'adres': 'os. Pod Lipami 23', 'wzrost':'172'}]


def wybierz_pelnoletnich(osoby):
    return [osoba for osoba in osoby if osoba['wiek'] >= 18]


def wyswietl_osoby(osoby):
    for osoba in osoby:
        print(osoba)


print(wybierz_pelnoletnich(moj_slownik))
