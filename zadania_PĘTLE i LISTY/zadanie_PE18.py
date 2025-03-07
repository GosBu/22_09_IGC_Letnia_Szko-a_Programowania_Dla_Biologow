# PE18 Stwórz listę która będzie zawierała tylko dodatnie elementy z listy a (wykorzystaj wyrażenie
# listowe)

list_a = [2, 56, 3, -2, 0, -1.6, 7, 230, 43, -7]

wyrazenia_dodatnie = [x for x in list_a if x > 0]
print(wyrazenia_dodatnie)
