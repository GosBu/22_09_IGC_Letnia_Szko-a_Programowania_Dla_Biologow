# FU12 Posortuj listę osób z zadania SL2 podług wieku oraz drugiej litery imienia.

moj_slownik = [{'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 31, 'adres': 'Al.Krakwoskie 15', 'wzrost': '176'},
               {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Al.Ujazdowskie 10', 'wzrost':'160'},
               {'imie': 'Aldona', 'nazwisko': 'Buczkowska', 'wiek': 20, 'adres': 'ul. Powstancow Wielkopolsich 12/1', 'wzrost':180},
               {'imie': 'Dorota', 'nazwisko': 'Poniatowska', 'wiek': 20, 'adres': 'os. Batorego 12/150', 'wzrost':168},
               {'imie': 'Kasia', 'nazwisko': 'Nowacka', 'wiek': 50, 'adres': 'os. Pod Lipami 23', 'wzrost':'172'}]

posortowane = sorted(moj_slownik, key=lambda x: (x['wiek'], x['imie'][1]))
print(posortowane)
