# 4.2 Dla zdania ‘Kobyła ma mały bok’ stwórz string zawierający posortowane litery (od a do z a
# następnie od z do a) bez uwzględniania wielkości liter.

zdanie = 'Kobyła ma mały bok'
lista = list(zdanie)
print(lista[0:])
sortowanie = sorted(lista)
print(sortowanie)
kolejnosc = ','.join(sortowanie)
print(kolejnosc)
zmiana = reversed.kolejnosc
print(list(zmiana))
