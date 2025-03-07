# PE3 Stwórz listę, która będzie zawierała liczby parzyste
# podzielne przez 3 i mniejsze niż 100 (liczby podzielne przez 3 mają resztę z dzielenia równą 0)

lista = []
for i in range(100):
    if i % 3 == 0 and i % 2 == 0:
        lista.append(i)
print(lista)

# lub
print(list(range(0, 100, 6)))
