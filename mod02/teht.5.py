
leiviskät = int(input("Anna leivistkat:  "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luotit: "))

# ensn selvitetään kuinka paljon on nauloja
naulatot = leiviskät * 20 + naulat

# sitten selvitetään kuinka paljon meillä on luoteja yhteensä
luoditot = naulatot * 32 + luodit

# nyt kun tiedetään määrän niin lasketaan massa ensin grammoina
grammatot = luoditot * 13.3
print(grammatot)

kg = grammatot / 100
print('kg' , kg)

kg = int(grammatot / 1000)
print('kg' , kg)

# on olemassa jakojäännösoperaatio (%), pelkän kokonaisluvun
kg = int(grammatot // 1000)
gr = grammatot % 1000
print(f'massa nykymittojen mukaan: {kg} ja {gr:.2f} grammaa')