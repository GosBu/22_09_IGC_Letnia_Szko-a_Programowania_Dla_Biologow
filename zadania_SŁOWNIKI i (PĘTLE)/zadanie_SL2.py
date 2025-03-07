# SL2 Stwórz bazę osób:
# 1) Stwórz listę słowników, gdzie będą zdefiniowani klienci (imię, nazwisko, wiek, adres, wzrost itd)
# 2) Obliczmy sumę wieku osób
# 3) Zmieńmy imię trzeciej osoby na 'Jan'

moj_slownik = [{'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 31, 'adres': 'Al.Krakwoskie 15', 'wzrost': '176'},
               {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Al.Ujazdowskie 10', 'wzrost':'160'},
               {'imie': 'Aldona', 'nazwisko': 'Buczkowska', 'wiek': 40, 'adres': 'ul. Powstancow Wielkopolsich 12/1', 'wzrost':180},
               {'imie': 'Dorota', 'nazwisko': 'Poniatowska', 'wiek': 20, 'adres': 'os. Batorego 12/150', 'wzrost':168},
               {'imie': 'Basia', 'nazwisko': 'Nowacka', 'wiek': 50, 'adres': 'os. Pod Lipami 23', 'wzrost':'172'}]

for imie in moj_slownik:
    print(imie)

suma_wieku = 0
for osoba in moj_slownik:
    suma_wieku += osoba['wiek']
print(suma_wieku)

moj_slownik[2]['imie'] = 'Jan'

for imie in moj_slownik:
    print(imie)
