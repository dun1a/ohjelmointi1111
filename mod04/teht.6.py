# π≈4n/N , jossa N on kaikkien pisteiden lukumäärä ja n yksikköympyrän sisälle osuvien pisteiden määrä jos pisteen kordinaatit toteuttavat epäyhtälön x^2+y^2<1, piste on ympyrässä
import random

N_arvo = int(input('Anna arvo N: '))
N = 100 # pisteiden kokonaismärä
n = 0 # ympyrään suvien pisteiden lukumäärä
counter = 0
while counter < N:
    counter += 1
    #arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'Arvot piste: {x}, {y}')
    print( x**2+y**2<1)
    if x**2+y**2<1:
        print('Piste on yksikönympyrässä.')
        N_arvo += 1

