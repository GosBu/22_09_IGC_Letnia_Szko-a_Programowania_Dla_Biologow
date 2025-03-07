import json
import requests

my_url = "https://tpsic.igcz.poznan.pl/trna/api-list/?format=json"
rensponse = requests.get(my_url, verify=False)
print(rensponse)
print(rensponse.status_code)
dane = rensponse.json()
print(dane)
nazwy = [x['name'] for x in dane]
print(nazwy)
