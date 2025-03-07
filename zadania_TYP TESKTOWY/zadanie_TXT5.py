# TXT5 Mamy zdanie i chcemy podzielić je w miejscu pierwszej znalezionej spacji
# używając splicingu (uzyskamy raz część przed spacją a raz od spacji do końca)

tekst = input('Wprowadź tekst: ')
print(tekst.split(sep=' ', maxsplit=1))
