"""
0/ 1/ 2
--------
3/ 4/ 5
--------
6/ 7/ 8

"""

plansza = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Nasze funkcje:
# wyswietl_plansze
# sprawdz_czy_wygrana
# sprawdz_czy_mozna
# graj

plansza = [0, 1, 2, 3, 4, 5, 6, 7, 8]       # plansz = list(range(9))

def wyswietl_plansze(plansza):
    print('{} | {} | {}\n----------\n{} | {} | {}\n----------\n{} | {} | {}\n----------'.format(*plansza))


wyswietl_plansze(plansza)


def czy_mozna(plansza, ruch):
    if ruch in plansza:
        return True
    return False


def graj():
    gracz = 'x'
    pola = plansza
    for j in range(9):
        ruch = -1
        while not czy_mozna(plansza, ruch):
            ruch = int(input('Podaj ruch: '))
        pola[ruch] = gracz
        if sprawdz_czy_wygrana(pola):
            print('Wygrałeś!')
            return
        gracz = 'o' if gracz == 'x' else 'x'

graj()
