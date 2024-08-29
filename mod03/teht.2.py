# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

hyttiluokka = input('Anna hyttiluokka: ')

if hyttiluokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
else:
    print('Virheellinen hyttiluokka')

hyttiluokka = input('Anna hyttiluokka: ')

if hyttiluokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
else:
    print('Virheellinen hyttiluokka.')

hyttiluokka = input('Anna hyttiluokka: ')
if hyttiluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
else:
    print('Virheellinne hyttiluokka.')

hyttiluokka = input('Anna hyttiluokka: ')
if hyttiluokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')