# FU8 Zmodyfikuj funkcję z wybranego zadania (np. FU4) dodając do niej typowanie statyczne
# odpowiedni docsring


def rysuj_ksztalt(ksztalt: str, wielkosc: int) -> None:
    """
    Funkcja rysująca trójkąt lubb kwadrat.
    :param ksztalt: trójkąt lub kwadrat
    :param wielkosc: wysokość trójkąta lubb kwadratu
    :return: None
    """
    if ksztalt == 'trojkat':
        for i in range(1, wielkosc+1):
            print('x' * 1)
    elif ksztalt == 'kwadrat':
        for i in range(1, wielkosc+1):
            print('x', * wielkosc)
