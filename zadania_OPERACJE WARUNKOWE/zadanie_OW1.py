# OW1 Sprawdź, czy wiek podany przez użytkownika pozwala zaklasyfikować osobę jako
# dorosłego.

wiek = int(input('Podaj wiek: '))
wynik = 'Osoba pełnoletnia' if wiek >= 18 else 'Osoba niepełnoletnia'
print(wynik)
