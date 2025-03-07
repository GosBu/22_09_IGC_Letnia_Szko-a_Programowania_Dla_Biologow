# 4.8 Sprawdź, czy zdanie ‘Kobyła ma mały bok’ jest palindromem

moje_zdanie = 'Kobyła ma mały bok'
male_litery = moje_zdanie.lower()       # string jest niemutowalny, wiec musimy przypisać ponownie do zmiennej. inaczej dzieje się z listą, która jest mutowalna
zdanie = male_litery.replace(' ', '')   # !
print(zdanie)
print(zdanie.startswith('kob'))
odwrocone_zdanie = reversed(zdanie)
print(odwrocone_zdanie)
print(zdanie.endswith('bok'))
