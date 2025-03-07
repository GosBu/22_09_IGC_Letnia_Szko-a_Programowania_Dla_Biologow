# TXT2 Stwórz tekst np. 'Ala ma kota' - zmień wielkość liter na duże, małe, tak żeby
# wszystkie wyrazy zaczynały się od dużej litery i tak żeby wszystkie wyrazy zaczynały się
# od małej i potem litery były duże np. aLA

tekst = 'Ala ma kota'
print(tekst.title())
print(tekst.lower())
print(tekst.lower()
      .replace('la', 'LA')
      .replace('ma', 'mA')
      .replace('ota', 'OTA'))


#dodatkowe: sekwencja i policzenie wystepowania C i G. WAŻNE 

sekwencja = 'ATATGCGCTGCTAGCATATATAGCTGCCCGATCA'
print(sekwencja.count('C') + sekwencja.count('G') / len(sekwencja))
