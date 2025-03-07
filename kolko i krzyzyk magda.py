pola = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def wyswietl_plansze(pola):
    print(10*'-')
    print('\\', pola[0], '\\', pola[1],'\\', pola[2], '\\')
    print(10*'-')
    print('\\', pola[3], '\\', pola[4], '\\', pola[5], '\\')
    print(10 * '-')
    print('\\', pola[6], '\\', pola[7], '\\', pola[8], '\\')
    print(10 * '-')



wyswietl_plansze(pola)

def sprawdz_czy_mozna(pola, pole):
    if pole in pola:
        return True
    return False


print(wyswietl_plansze(pola))

WYGRANE = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # poziomo
           (0, 3, 6), (1, 4, 7), (2, 5, 8),  # pionowo
           (0, 4, 8), (2, 4, 6)]  # po skosie
def sprawdz_czy_wygrana(pola):
    """
    Sprawdza czy po ostatnim ruchu nastąpiła wygrana.

    :param plansza: plansza do gry (lista od 0 do 8)
    :return: True jeśli wygrana False w przeciwnym przypadku
    """
    for potencjalna_wygrana in WYGRANE:
        pos1 = potencjalna_wygrana[0]  # pozycja na planszy do sprawdzenia
        pos2 = potencjalna_wygrana[1]
        pos3 = potencjalna_wygrana[2]
        if pola[pos1] == pola[pos2] == pola[pos3]:
            return True
    return False  # ważne - poza pętlą tak żeby sprawdzić wszystkie

def graj():
    znak = 'x'
    while True:
        pole = int(input('Wpisz pole: '))
        #znak = input('Wpisz znak: ')
        if not sprawdz_czy_mozna(pola, pole):
            print('Pole zajęte')
            continue
        # teraz to co można gdy pole ok
        pola[pole] = znak
        wyswietl_plansze(pola)
        if sprawdz_czy_wygrana(pola):
            print(f'Wygrana gracza {znak}')
            break
        znak = 'x' if znak =='o' else 'o'
        # czy remis:
        if set(pola) == {'o', 'x'}:
            print('remis')
            break

print(graj())
