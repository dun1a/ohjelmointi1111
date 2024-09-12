names = set()

name = input('Anna nimesi: ')

while name !='':
    name = input('Anna nimesi: ')
    print(name)
    if name =='':
        break

    if name in names:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')
        names.add(name)

print(names)










