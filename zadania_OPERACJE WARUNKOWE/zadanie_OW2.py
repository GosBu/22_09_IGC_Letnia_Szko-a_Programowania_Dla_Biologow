# OW2 Stwórz kod, który w zależności od podanego z klawiatury zwierzęcia (kot, pies, ptak)
# wypisze rekomendowany rodzaj karmy (karma dla kotów, psów, ptaków odpowiednio)

zwierze = input('Podaj zwierze: ')
# wskazane_zwierze = {'karma dla kota':'kotów',
                    # 'karma dla psa':'psów',
                    # 'karma dla ptaków':'ptak'}

if zwierze == 'kot':
    print('karma dla kotów')
if zwierze == 'pies':
    print('Karma dla psów')
elif zwierze == 'ptak':
    print('Karma dla ptaków')
else:
    print('Przepraszamy, nie mamy wybranej karmy.')
