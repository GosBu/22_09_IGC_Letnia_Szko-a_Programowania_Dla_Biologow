# W trzeci pliku (start.py) chcemy je zaimportować i utworzyć osobę o konkretnym adresi
from zadanie_moduly_1_1 import Osoba
from zadanie_moduly_1_2 import Adres

nowy_adres = Adres('Nad potokiem', 'Kraków')

nowa_osoba = Osoba('Jola', 'Nowak', 20, nowy_adres)
print(nowa_osoba)
