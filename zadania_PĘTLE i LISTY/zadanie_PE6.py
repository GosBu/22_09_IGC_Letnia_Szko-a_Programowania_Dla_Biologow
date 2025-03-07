# PE6 Wypisz wartość sinusa dla kątów w zakresie 1 - 90
from math import sin, radians

print(sin(90))

i = 0
while i < 91:
    print(sin(radians(i)))
    i += 1
