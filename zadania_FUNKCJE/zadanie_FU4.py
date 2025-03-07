# FU4 Stwórz funkcję, która przyjmie jako argumenty kształt (trójkąt/kwadrat) i wielkość i na ich
# podstawie wyświetli na ekranie odpowiedni kształt. Rozbuduj funkcję dodając parametr, który
# określi jakim znakiem ma być rysowany ten kształt.


def rysuj_ksztalt(ksztalt, wielkosc):
    if ksztalt == 'trojkat':
        for i in range(1, wielkosc+1):
            print('x' * i)
    elif ksztalt == 'kwadrat':
        for i in range(1, wielkosc+1):
            print('x', * wielkosc)


rysuj_ksztalt('trojkat', 5 )
rysuj_ksztalt('kwadrat', 6)

