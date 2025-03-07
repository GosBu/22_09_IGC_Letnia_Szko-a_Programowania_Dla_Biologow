# PE20 Dla listy a:
# a = ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]
# i listy b:
# b = ['cde', 'b', 33, 'gh', 'g']
# c = []
# zrób pętlę w której sprawdzimy czy każdy element z listy b znajduje się w liście a
# i jeśli nie to doda go do listy c

a = ['a', 'cde', 'b', 33, 4.14, 'd', 4, 1]
b = ['cde', 'b', 33, 'gh', 'g']
c = []

for element in b:
    if element not in a:
        c.append(element)
print(c)
