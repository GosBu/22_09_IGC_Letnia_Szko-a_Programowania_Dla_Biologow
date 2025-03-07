# PE2 Wykorzystując instrukcje sterujące (break, continue) stwórzmy pętlę, która która dla zmiennej
# (np. i) zmieniającej się od 0 do 1000 wyświetli wartość i, ale:a) jeśli wartość jest podzielna przez 3
# to nie wyświetli tej wartości
# b) jeśli wartość jest podzielna przez 77 to przerwie działanie pętli

for element in range(0, 1001):
    if element % 3 == 0:
        continue
    if element % 77 == 0:
        break
    print(element)
