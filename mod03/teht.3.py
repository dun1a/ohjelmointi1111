#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli_yks = 'nainen'
sukupuoli_kaks = 'mies'
sukupuoli = input('Anna sukupuoli: ')
hemoglobiiniarvo = int(input('Anna hemoglobiiniarvo: '))

if sukupuoli == sukupuoli_yks and hemoglobiiniarvo >117 and hemoglobiiniarvo <175:
    print('Hemoglobiiniarvo on normaali.')

elif sukupuoli == sukupuoli_kaks and hemoglobiiniarvo >134 and hemoglobiiniarvo <195:
            print('Hemoglobiiniarvo on normaali.')

else:
    if sukupuoli_yks:
        if hemoglobiiniarvo < 117:
            print('Hemoglobiini arvo on alhainen.')
            if hemoglobiiniarvo > 175:
                print('Hemoglobiini arvo korkea.')
    if sukupuoli_kaks:
            if hemoglobiiniarvo < 134:
                print('Hemoglobiiniarvo on alhainen.')
                if hemoglobiiniarvo > 195:
                    print('Hemoglobiiniarvo on korkea.')


