# PE12 Narysuj trójkąt
# XX
# X
# XXX

wielkosc = int(input('Wprowadź wielkość: '))
linia = ''
for i in range(wielkosc):
    linia += 'X'
    print(linia)

# lub
wielkosc = int(input('Wprowadź wielkość: '))
for i in range(wielkosc):
    print('X'*(i+1))
