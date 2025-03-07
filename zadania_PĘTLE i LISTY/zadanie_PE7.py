# PE7 Wypisz wartość sinusa /cosinusa dla kątów w zakresie 1 – 90, rodzaj funkcji
# trygonometrycznej użytkownik ma podać z klawiatury

from math import sin, cos, radians
funkcja = sin if input('Podaj funkcję sin/ cos: ') == 'sin' else cos
for i in range(1, 91):
    print(funkcja(radians(i)))
