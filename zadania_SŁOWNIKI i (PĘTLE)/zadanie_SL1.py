# SL1 Stwórz słownik danych osobowych klienta
# odpytaj klienta o jego imię nazwisko i wiek, dodaj je do słownika

imie = input('Podaj imie: ')
nazwisko = input('Podaj nazwisko: ')
wiek = int(input('Podaj wiek: '))

moj_slownik = dict(imie = imie, nazwisko=nazwisko, wiek=wiek)

print(moj_slownik)
