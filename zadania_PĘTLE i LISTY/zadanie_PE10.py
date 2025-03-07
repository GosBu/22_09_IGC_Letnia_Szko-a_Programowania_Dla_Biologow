# PE10 Stwórz kwadrat o określonej wielkości (wprowadzanej z klawiatury) z litery X.
# Przykładowo dla wielkości 3 kwadrat powinien wyglądać jak poniżej:
# XXX
# XXX
# XXX
# 1) dodając pojedyncze litery X do siebie i printując w zagnieżdżonych pętlach
# 2) wykorzystując zamiast jednej z pętli mnożenie stringów

wielkosc = int(input('Wprowadź wielkość: '))
for j in range(wielkosc):
    linia = ''
    for i in range(wielkosc):
        linia += 'X'
    print(linia)

# 2)
wielkosc = int(input('Wprowadź wielkość: '))
for a in range(wielkosc):
    print('X'*wielkosc)
