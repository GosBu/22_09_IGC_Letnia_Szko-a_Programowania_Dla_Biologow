# 4.4 Do listy [2, 4, 6, 12, 16] dodaj listę [1, 3, 5] a następnie stwórz nową, posortowaną listę
# zawierającą wszystkie elementy

moja_lista = [2, 4, 6, 12, 16]
moja_lista += [1,3,5]     # gdyby trzeba byłp dodać tuplę lub inny tp, to trzeba użyś extend()
print(moja_lista)
print(sorted(moja_lista))
