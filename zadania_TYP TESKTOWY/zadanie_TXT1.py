# TXT1 Stwórz program, który policzy ile razy w podanym przez użytkownika zdaniu znajduje się
# literka małe a? Ile razy w podanym zdaniu znajduje się mała lub duża litera a?

zdanie = input('Podaj zdanie: ')
a = zdanie.count('a')
zmiana_na_male = zdanie.lower()
b = zmiana_na_male.count('a')
print(zdanie)
print(a)
print(b)
