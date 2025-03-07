# 5.4 Stwórz listę, która będzie zawierała unikalne elementy z dwóch list:
# ['ala', 'ma', 'kota'], ['kota', 'nie', 'ma', 'u', 'kasi']
# wynik ma być w stylu:
# ['ala', 'kota', 'nie', 'ma', 'u', 'kasi']
# bez wykorzystania pętli

# Sposób pierwszy
moja_lista_1 = ['ala', 'ma', 'kota']
moja_lista_1 += ['kota', 'nie', 'ma', 'u', 'kasi']
moj_zbior = set(moja_lista_1)
print(list(moj_zbior))

# Sposób drugi
moja_lista_1 = ['ala', 'ma', 'kota']
moja_lista_2 = moja_lista_1 + ['kota', 'nie', 'ma', 'u', 'kasi']
moj_zbior = set(moja_lista_2)
print(list(moj_zbior))

# Sposób trzeci
moj_zbior_1 = set(['ala', 'ma', 'kota'])
moj_zbior_2 = set(['kota', 'nie', 'ma', 'u', 'kasi'])
moj_zbior_finalny = moj_zbior_2 | moj_zbior_1
print(list(moj_zbior_finalny))
