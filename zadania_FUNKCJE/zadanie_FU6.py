# FU6 Stwórz funkcję lambda, którą użyjesz w funkcji filter, żeby ze zbioru [3, 4, 2, 1, 9] wybrać
# liczby parzyste

zbior = [3, 4, 2, 1, 9]
parzyste = filter(lambda x: x % 2 == 0, zbior)
print(list(parzyste))       # lub print(*parzyste)

# krócej

print(*filter(lambda x: x % 2 == 0, zbior))
