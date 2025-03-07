# OW3 Stwórz kod, który pozwoli na porównanie zmiennej a i zmiennej b wprowadzonych z
# klawiatury

a = float(input('Podaj zmienna a: '))
b = float(input('Podaj zmienna b: '))

# porownanie = 'zmienna a wieksza od zmiennej b' if a > b else 'zmienna a nie jest wieksza od zmiennej b'
# print(porownanie)

if a > b:
    print('zmienna a wieksza od b')
elif a < b:
    print('zmienna a jest mniejsza od b')
else:
    print('zmienna a jest rowna zmniennej b')
