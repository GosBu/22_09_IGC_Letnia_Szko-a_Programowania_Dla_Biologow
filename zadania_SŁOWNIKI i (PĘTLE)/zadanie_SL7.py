# SL7 Dla bazy z zadania 2 stwórz słownik, gdzie kluczem będzie miejscowość a wartością będzie
# lista osób mieszkająca w tej miejscowości

moj_slownik = [{'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 31, 'adres': 'Warszawa', 'wzrost': '176'},
               {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Warszawa', 'wzrost':'160'},
               {'imie': 'Aldona', 'nazwisko': 'Buczkowska', 'wiek': 40, 'adres': 'Kraków', 'wzrost':180},
               {'imie': 'Dorota', 'nazwisko': 'Poniatowska', 'wiek': 20, 'adres': 'Poznań', 'wzrost':168},
               {'imie': 'Basia', 'nazwisko': 'Nowacka', 'wiek': 50, 'adres': 'Poznań', 'wzrost':'172'}]
keys = ['city']
dict_city = {}

for osoba in moj_slownik:
    if osoba['adres'] not in dict_city.keys():
       dict_city[osoba['adres']] = []
    dict_city[osoba['adres']].append(osoba)
for adres in dict_city:
    print(adres, dict_city[adres])
