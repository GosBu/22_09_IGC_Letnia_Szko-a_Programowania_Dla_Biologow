# 5.2 Stwórz zbiór unikalnych liczb spośród wielokrotności liczby 3 do 30 i dodatkowo
# wielokrotności liczby 2 do 30

moj_zbior = range(3,31, 3)
print(set(moj_zbior))

moj_zbior_2 = range(2,31, 2)
print(set(moj_zbior_2))

print(set(moj_zbior) | set(moj_zbior_2))
