# WY1 Stwórz kod pobierający liczby od użytkownika, który w przypadku podania liter przechwyci
# wyjątek a następnie poinformuje o problemie użytkownika

liczba = input('Podaj liczbę: ')
try:
    int(liczba)
except TypeError:
        print('Błędny typ, musisz podać int')
