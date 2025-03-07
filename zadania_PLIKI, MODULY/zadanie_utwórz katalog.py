# W katalogu x utwórz (ręcznie) pliki a.txt, b.txt., c.txt. Uwórz skrypt,
# który stworzy pełne ścieżki dostępu do tych plików, wyświetli je i przekopiuje wszystkie pliki
# do nowego katalogu (trzeba utworzyć) wynik

import os

katalog = os.path.dirname(__file__)
nazwa_plikow = [plik for plik in os.listdir(katalog) if plik.endswith('txt')]

# alternatywne rozwiązanie
# import glob
# os.chdir(katalog)
# nazwa_plikow = glob('*.txt')

full_paths = [os.path.join(katalog, nazwa_pliku) for nazwa_pliku in nazwa_plikow]
print(full_paths)

import Bio

