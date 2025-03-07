# ZO6 Stwórz kod, który obliczy na jaką wysokość wzniesie się samolot po x minutach (podanych przez użytkownika), jeśli prędkość wznoszenia to 12 m/s. Pomiń maksymalną wysokość.
x = int(input('Podaj czas w minutach: '))
SECOND = 1
MINUTE = 60
METR = 1
wysokosc = x * MINUTE * 12 * METR

print(wysokosc)
