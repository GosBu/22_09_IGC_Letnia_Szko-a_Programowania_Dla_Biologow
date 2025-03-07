# W drugim klasą ma być Adres

class Adres:
    def __init__(self, ulica, miasto):
        self.ulica = ulica
        self.miasto = miasto

    def __str__(self):
        return f'[Adres]{self.ulica}, {self.miasto}'

adres_1 = Adres('Poznańska', 'Poznań')
print(adres_1)
