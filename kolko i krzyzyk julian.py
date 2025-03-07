# Gra w kółko i krzyżyk
plansza = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# wyswietl_plansze
def wyswietl_plansze(plansza):
    print('{} | {} | {}\n---------\n'
          '{} | {} | {}\n---------\n'
          '{} | {} | {}'.format(*plansza))


wyswietl_plansze(plansza)

WYGRANE = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # poziomo
           (0, 3, 6), (1, 4, 7), (2, 5, 8),  # pionowo
           (0, 4, 8), (2, 4, 6)]  # po skosie

def sprawdz_czy_wygrana(plansza):
    """
    Sprawdza czy po ostatnim ruchu nastąpiła wygrana.

    :param plansza: plansza do gry (lista od 0 do 8)
    :return: True jeśli wygrana False w przeciwnym przypadku
    """
    for potencjalna_wygrana in WYGRANE:
        pos1 = potencjalna_wygrana[0]  # pozycja na planszy do sprawdzenia
        pos2 = potencjalna_wygrana[1]
        pos3 = potencjalna_wygrana[2]
        if plansza[pos1] == plansza[pos2] == plansza[pos3]:
            return True
    return False  # ważne - poza pętlą tak żeby sprawdzić wszystkie

# sprawdz czy mozna
def sprawdz_czy_mozna(plansza, ruch):
    if ruch in plansza:
        return True
    return False


# graj
def graj():
    gracz = 'x'
    pola = plansza
    for j in range(9):
        ruch = -1
        while not sprawdz_czy_mozna(pola, ruch):
            ruch = int(input(f'Graczu {gracz}, podaj poprawny ruch: '))
        pola[ruch] = gracz
        wyswietl_plansze(pola)
        if sprawdz_czy_wygrana(pola):
            print(f'Wygrana gracza {gracz}')
            return
        gracz = 'o' if gracz == 'x' else 'x'
    print('REMIS')


graj()
