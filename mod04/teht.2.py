#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm


tuuma_cm = 2.54
# senttimetri = 0
tuuma = float(input('Anna tuumia: '))

while tuuma > 0:
    senttimetrit = tuuma * tuuma_cm
    print(senttimetrit)
else:
    if tuuma < 0:
        print('Ohjelma loppuu.')

