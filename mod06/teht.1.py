import random


def roll_dice():
    return random.randint(1, 6)

'''
print(roll_dice())

while roll_dice() != 6:
    print(roll_dice())
'''
# print('------------')

# melkein sama juttu, tää tulostaa kutosen lopussa, mutta yllä oleva ei
result = 0
while result != 6:
    result = roll_dice()
    print(result)


