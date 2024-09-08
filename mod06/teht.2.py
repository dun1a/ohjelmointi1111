import random

def roll_dice(maxim):
    return random.randint(1, maxim)

maximi = int(input('mikä on maxim: '))

result = 0
while result != maximi:
    result = roll_dice(maximi)
    print(result)
    

