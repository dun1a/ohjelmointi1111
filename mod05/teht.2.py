
luvut = []

luku1 = input('Anna luku: ')
while luku1 != '':
    luvut.append(int(luku1))
    luku1 = input('Anna luku: ')

#print(luvut)

luvut.sort(reverse=True)
for numero in luvut:
    print(numero)















