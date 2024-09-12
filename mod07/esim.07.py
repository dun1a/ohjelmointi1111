# monikko ()

#########################
print('\nMONIKKO ()\n')

# Monikko (tuple) on "kukin lista jota ei voi muokata"

minun_lista = [1,2,3,4,5,6]
print(minun_lista)

#minun_monikko = (1,2,3,4,5,6)
minun_monikko = 1,2,3,4,5,6
print(minun_monikko)

minun_monikko2 = (1,2,(3,4),5,'kuusi')
print(minun_monikko2)

# luetaan ensimmäinen alkio
print(minun_monikko2[0])
print(minun_monikko[0])

# yritetään muokata eka alkio numeroksi 0 ja lisätä loppuun 7
# listan sisältöä voi muokata, mutable
minun_lista[0] = 0
minun_lista.append(7)
print(f'muokattu lista {minun_lista}')

print('-----------------')

# monikon sisältöä EI voi muokata, eli imutable
# minun_monikko[0] = 0
'''
# monikko on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jana on luonteeltaan staattinen:
# tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen

viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = (viikonpäivät[järjestysnumero-1])
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''
print('----------------')

# monikko läpikäynti kuten listan
for i in minun_monikko:
    print(i)

# monikkon arvojen purku muuttujiin
hedelmät = ('mandariini', 'ananas', 'mansikka')
# (eka, toka, kolmas) = ('mandariini', 'ananas', 'mansikka')
(eka, toka, kolmas) = hedelmät
print(eka)

print('\nMonikon voi antaa funktiolla parametrina: ')
sanalista = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')
def tulosta_monikko(sanalista):
    for i in sanalista:
        print(i)

tulosta_monikko(sanalista)
tulosta_monikko(hedelmät)

# monikko funktion paluuarvona
import random

def heitä():
    (eka, toka) = random.randint(1,6), random.randint(1,6)
    #eka = random.randint(1,6)
    #toka = random.randint(1, 6)
    return (eka, toka)

(noppa1, noppa2) = (eka, toka)
noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

print()
print('JOUKKO()\n')

# JOUKKO eli set {}

joukko = {1,2,3,4,5,6}

# joukko merkitään aaltosulkeilla
print(joukko)

print(f'numero 6 voi esiintyä listassa usesti: ')

minun_numerolista = [6,2,3,4,5,6]
print(minun_numerolista)
print()
print(f'numero 6 voi esiintyä listassa usesti: ')
minun_monikkonumerolista = (6,2,3,4,5,6)
print(minun_monikkonumerolista)
print()
print(f'numero 6 voi esiintyä listassa usesti: ')
minun_joukko = {6,2,3,4,5,6}
print(minun_joukko)

# yllä oleva ei tuota virhettä, kuten ei add-metodi

minun_joukko.add(8)
print(minun_joukko)
minun_joukko.remove(8)
print(minun_joukko)


# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.
print()
# koodiesimerkki, järjestys voi muuttua printatessa

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

# alkiot iteroidaan läpi for/in rakenteella
for p in pelit:
    print(p)
    # checkataan löytyykö cluedo, jos löytyy printtaa jotain
    if p == 'Cluedo':
        print('Cluedo löytyi!!!!!')

# if / in haku toimii kuten listoissa
if 'Monopoli' in pelit:
    print('Monopoli löytyi!!')

# tyjä joukko luodaan edellä esitetystä poiketen set-funktioin avulla
print()

autolista = []
autolista.append('Audi')
print(autolista)

# tästä tulee sanakirja eli dictionary
autojoukko = {}
print(type(autojoukko)) # tässä <class dict>

# tyhjä joukko luodaan edellä esitetyistä poiketen set-funktion avulla.
autojoukko = set()
autojoukko.add('Audi')
print(type(autojoukko)) # tässä on <class 'set'>
print(autojoukko)

print('\nSANAKIRJA {} \n')

# Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.

#Sanakirjaan voidaan tallentaa avain-arvopareja.

oppilaat = {'Fesse': 15,'Menes': 16, 'Tiiz': 19, 'Mothah': 50}
print(oppilaat)

# mitä ovat tietueet eli items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa
print(oppilaat.keys())

# mitä ovat arvoja sanakirjassa
print(oppilaat.values())

print()
# kun sanakirjaa käydään läpi for / in rakenteella:

#tietueet eli avain-arvoparit
for i in oppilaat.items():
    print(i)

# oppilaat = {'Fesse': 15,'Menes': 16, 'Tiiz': 19, 'Mothah': 50}
# yksittäisen arvon haku avaimen avulla

avain = 'Menes'
print(oppilaat[avain]) # etsii avaimella Menes sen arvoa joka on 16
# sama asia kuin print(oppilaat['Menes'])

# etsii kaikki arvot
# arvot
for i in oppilaat:
    print(oppilaat[i])

# if / in rakenteella voidaan myös hakea sanakirjasra tietoa

nimi = input('Anna nimi, niin etsin sen sanakirjasta jos löytyy: ')
if nimi in oppilaat:
    print(f'Eyo oppilas {nimi} löytyi ja hänen ikä on {oppilaat[nimi]}')
print()

# kun olemassa olevaan sanakirjaan lisätään arvo, köytetään notaatiota sanakirja[avain] = arvo

# listätään uusi oppilas mikäli ei löydy
# jos avain löytyy, se muokkaa olemassa olevaa, muuten luodaan uusi

oppilaat['Hannah'] = 19
print(oppilaat)
print()

nimet = ['Menes', 'Fesse']
numerot = ['050-1234567', '040-1112223']

print(f'{nimet[0]}, numerot: {numerot[0]}')

yhteystiedot = {'Menes': '050-1234567', 'Fesse': '040-1112223'}
#print(f'Menesin numero: {yhteystiedot['Menes']}')
hakusana = input('Puhelinnumerohaku, anna nimi: ')

# listojen avulla, selvitetään ensin oikea indeksi
index = nimet.index(hakusana)
print(f'{hakusana}, numero: {numerot[index]}')

# sanakirjalla, hyödynnetään avainta
print(f'{hakusana}, numero: {yhteystiedot[hakusana]}')

# extra: moniulotteinen
yhteystiedot = {
    'Menes': {'puh':'050-1234567', 'osoite': 'porvoonkatu 4'},
    'Fesse': {'puh':'040-1112223', 'osoite': 'porvoonkatu 4'}
}
print(f'Menes osoite{yhteystiedot["Menes"]["osoite"]}')