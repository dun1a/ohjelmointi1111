#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerrankaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

# how many dice to roll
import random

total = 0
dice_count = int(input('Montako noppaa laitetaan?: ')) # heittojen määrä
for i in range(dice_count):
    total = total + random.randint(1, 6)
print(f'Noppien solmälukujen summa on {total}')

'''
total = 0
result_history = [] # extra
dice_count = int(input('Montako noppaa laitetaan?: ')) # heittojen määrä
for i in range(dice_count):
    result = random.randint(1, 6)
    total = total + result
    result_history.append(random.randint(1, 6))
print(f'Noppien solmälukujen summa on {total}, nopat {result_history}')
'''












