
username = 'python'
password = 'rules'

käyttäjätunnus = input('Anna käyttäjätunnus: ')
salasana = (input('Anna salasana: '))
max_kerrat = 5
kokeilut = 0

while kokeilut < max_kerrat:
    käyttäjätunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    if käyttäjätunnus == username and salasana == password:
        print('Welcom')
    else:
        if kokeilut == max_kerrat:
            print('Access denied.')



