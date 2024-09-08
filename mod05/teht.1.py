#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerrankaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

total = 0
dice_count = int(input('Montako noppaa laitetaan?: ')) # heittojen määrä
for i in range(dice_count):
    total = total + random.randint(1, 6)
print(f'Noppien solmälukujen summa on {total}')












