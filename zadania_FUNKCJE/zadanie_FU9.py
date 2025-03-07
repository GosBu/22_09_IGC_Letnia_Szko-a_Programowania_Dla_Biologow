# FU9 Stwórz funkcję pełnoletni, która przyjmie pojedynczą osobę (z zadania SL2) I zwróci True
# jeśli osoba ma co najmniej 18 lat

osoba1 = {'imie': 'Tomek', 'nazwisko': 'Kowalski', 'wiek': 31, 'adres': 'Al.Krakwoskie 15', 'wzrost': '176'}
osoba2 = {'imie': 'Kasia', 'nazwisko': 'Nowak', 'wiek': 25, 'adres': 'Al.Ujazdowskie 10', 'wzrost':'160'}


def wsprawdz_pelnoletnosc(osoba):
    if osoba['wiek'] >= 18:
        return True
    else:
        return False


print(wsprawdz_pelnoletnosc(osoba1))



# lub


def czy_pelnoletni(osoba):
    return osoba['wiek'] >= 18


print(czy_pelnoletni(osoba1))
