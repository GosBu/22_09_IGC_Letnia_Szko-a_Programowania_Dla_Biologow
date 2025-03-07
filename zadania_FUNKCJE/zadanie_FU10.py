# FU10 Stwórz funkcję, która przyjmie listę osób (z zadania SL2) oraz funkcję z zadania FU9 i
# wykorzysta tą funkcję do wyfiltrowania osób, które są pełnoletnie

moj_slownik = [{'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 31, 'adres': 'Al.Krakwoskie 15', 'wzrost': '176'},
               {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Al.Ujazdowskie 10', 'wzrost':'160'},
               {'imie': 'Aldona', 'nazwisko': 'Buczkowska', 'wiek': 40, 'adres': 'ul. Powstancow Wielkopolsich 12/1', 'wzrost':180},
               {'imie': 'Dorota', 'nazwisko': 'Poniatowska', 'wiek': 20, 'adres': 'os. Batorego 12/150', 'wzrost':168},
               {'imie': 'Basia', 'nazwisko': 'Nowacka', 'wiek': 50, 'adres': 'os. Pod Lipami 23', 'wzrost':'172'}]


def czy_pelnoletni(osoba):
    return osoba['wiek'] >= 18


def filtorwanie_pelnoletnich(moj_slownik, funkcja):
    return [osoba for osoba in moj_slownik if funkcja(osoba)]


print(filtorwanie_pelnoletnich(moj_slownik, czy_pelnoletni))
