# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen,ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.


pituus = int(input('Anna kuhan pituus senttimetreinä: '))

alimitta = 37
if pituus < alimitta:
    puuttuu = alimitta - pituus
    print('Kuha on alimittainen. Laske kuha takaisin järveen.')
    print(f"Kuha on {puuttuu} cm liian lyhyt.")

