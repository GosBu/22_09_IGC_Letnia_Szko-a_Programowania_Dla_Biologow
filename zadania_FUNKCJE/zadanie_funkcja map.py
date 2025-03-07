# Mamy listę stopni [4, 12, 25, 32]. Chcemy uzyskać Kelwiny (+273). Chcemy użyć funkcji map i lambda

temp_Celsiusze = [4, 12, 25, 32]
temp_Kalwiny = list(map(lambda x: x + 273, temp_Celsiusze))
print(temp_Kalwiny)
