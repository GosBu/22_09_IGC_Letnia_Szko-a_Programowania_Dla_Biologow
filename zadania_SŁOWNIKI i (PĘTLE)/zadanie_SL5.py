# SL5 Dla każdej osoby w bazie z zadania 2 dodaj do wieku wartość 1

moj_slownik = [{'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 31, 'adres': 'Al.Krakwoskie 15', 'wzrost': '176'},
               {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Al.Ujazdowskie 10', 'wzrost':'160'},
               {'imie': 'Aldona', 'nazwisko': 'Buczkowska', 'wiek': 40, 'adres': 'ul. Powstancow Wielkopolsich 12/1', 'wzrost':180},
               {'imie': 'Dorota', 'nazwisko': 'Poniatowska', 'wiek': 20, 'adres': 'os. Batorego 12/150', 'wzrost':168},
               {'imie': 'Basia', 'nazwisko': 'Nowacka', 'wiek': 50, 'adres': 'os. Pod Lipami 23', 'wzrost':'172'}]

for osoba in moj_slownik:
    osoba['wiek'] += 1
    print(osoba['wiek'])
