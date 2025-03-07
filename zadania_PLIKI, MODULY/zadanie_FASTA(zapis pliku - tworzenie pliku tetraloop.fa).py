# Zapisz do pliku o nazwie tetraloop.fa
naglowek = '>Testowy motyw'
sekwencja = 'GNRA'

with open('tetraloop.fa', mode='w', encoding='utf-8') as f:
    f.write('>Testowy motyw' + '\nGNRA')
