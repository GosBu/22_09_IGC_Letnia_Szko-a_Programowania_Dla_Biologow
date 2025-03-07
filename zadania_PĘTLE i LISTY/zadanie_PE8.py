# PE8 Stwórz tabliczkę mnożenia, która w nieskończoność będzie wyświetlała
# tabliczkę mnożenia dla kolejnych liczb podawanych przez użytkownika
# liczby muszą być w przedziale <1, 10>

while True:
    cyfra = int(input('Wprowadź cyrę: '))
    for i in range(1, 10):
        print(f'{i} * {cyfra} = {i * cyfra}')
