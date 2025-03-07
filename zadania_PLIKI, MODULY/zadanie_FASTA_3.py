# Otwórz plik FASTA.txt. Zapisz do pliku fasta_out sekwencję z pliku FASTA.txt podzieloną co 10 nukleotydów
# nagłówki dowolne (mogą być indeksy)

with open('FASTA.txt', mode='r', encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()
    print(lines)
    naglowek = lines[0]
    sekwencja = ''.join(lines[1:])
    fragmenty = []
    dlugosc_tekstu = len(content)
    x = 10
    while x < dlugosc_tekstu:
        fragmenty.append(content[x: x+10])
        print(fragmenty)
        x += 10
with open('fasta_out', mode='w', encoding='utf-8') as f:
    f.write(str(fragmenty))
