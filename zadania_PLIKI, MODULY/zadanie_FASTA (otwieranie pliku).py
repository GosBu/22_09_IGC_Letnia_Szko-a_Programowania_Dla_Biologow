# Otwórz plik. Podziel na nagłówek i sekwencję

with open('FASTA.txt', mode='r', encoding='utf-8') as f:
    # print(f.read())
    content = f.read()
    lines = content.splitlines()
    print(lines)
    naglowek = lines[0]
    sekwencja = ''.join(lines[1:])
    print(naglowek)
    print(sekwencja)
