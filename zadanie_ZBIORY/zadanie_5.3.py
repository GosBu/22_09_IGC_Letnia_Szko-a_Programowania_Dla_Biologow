# 5.3 Stwórz zbiór liczb które są wielokrotnością liczby 3 mniejszą niż 31 i nie są jednocześnie
# wielokrotnością liczby 2

moj_zbior = set(range(3, 31, 3))
moj_zbior_2 = set(range(4, 31, 2))
print(moj_zbior - moj_zbior_2)
