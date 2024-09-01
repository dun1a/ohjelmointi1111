import random

# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.


oikea_arvonta = random.randint(1, 10)

while True:
    arvaus = int(input('Anna arvaus: '))
    if arvaus > oikea_arvonta:
        print('Liian suuri arvaus.')
    else:
        if arvaus < oikea_arvonta:
            print('Liian pieni arvaus.')
        else:
            if arvaus == oikea_arvonta:
                print('Oikein.')


