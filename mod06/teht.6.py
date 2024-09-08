import math

def pitsa(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * (sade **2)
    yksikköhinta = hinta / pinta_ala
    halkaisija1 = int(input('Anna halkaisija: '))
    hinta1 = int(input('Anna hinta: '))
    halkaisija2 = int(input('Anna halkaisija: '))
    hinta2 = int(input('Anna hinta: '))

    return yksikköhinta

yksikköhinta = laske_yksikköhinta(halkaisija1, hinta1)
yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)






