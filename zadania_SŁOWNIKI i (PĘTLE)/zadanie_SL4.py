# SL4 Stwórz program do wydawania reszty za pomocą jak najmniejszej ilości monet i banknotów.
# Na podstawie wprowadzonej kwoty do zwrotu program ma zwrócić nominały i ich liczbę oraz
# informację ile jest banknotów a ile monet do zwrotu (wykorzystaj słownik, gdzie kluczem będzie
# nominał a wartością string ‘banknot’ lub ‘moneta’

kwota = float(input('Podaj kwote zaplaty: '))
nominaly = (500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)
banknoty_monety = {500: 'banknot', 200: 'banknot', 100: 'banknot', 50: 'banknot', 20: 'banknot', 10: 'banknot', 5: 'moneta', 2: 'moneta', 1: 'moneta', 0.5: 'moneta', 0.2: 'moneta', 0.1: 'moneta', 0.05: 'moneta', 0.02: 'moneta', 0.01: 'moneta'}
reszta = 434.75
wydane_nominaly = []
wydane_banknoty = 0
wydane_monety = 0

for nominal in nominaly:
    while reszta > nominal:
        wydane_nominaly.append(nominal)
        reszta -= nominal
        if banknoty_monety[nominal] == 'banknot':
            wydane_banknoty += 1
        else:
            wydane_monety += 1

print(wydane_nominaly)
print(wydane_banknoty, wydane_monety)
