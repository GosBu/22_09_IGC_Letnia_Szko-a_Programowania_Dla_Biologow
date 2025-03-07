# PE5 Dla zadanej listy:
# ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]
# dla wszystkich elementów prócz pierwszego i ostatniego wypisz ten element i jego typ
# przykładowo dla pierwszego elementu:
# a <type str>

lista = ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]

for element in lista[1:7]:
    print(element, type(element))
