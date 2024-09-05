
name ='Ville'
name2= 'Liisa'
name3 = 'Mina'
age1 = 3
age2 = 5
age3 = 22

print(f'Moi {name} ja ikäsi on {age1} vuotta')
print(f'Moi {name2} ja ikäsi on {age2} vuotta')
print(f'Moi {name3} ja ikäsi on {age3} vuotta')
print('------------------')

names = ['Ville', 'Liisa', 'Mina', 'Fesse', 'MIa']
ages = [age1, age2, age3, 34, 23]
print(names)
print(ages)


#names2 = [name, name2, name3]
#print(names2)

# lista npituus voidaan tarkitaa len() funktiolla
length = len(names)
print(f'Listan pituus on: {length}')

# alkioon viitataan indeksinumerolla
print(names[3])
print(f'Hei {names[3]} ikäsi on {ages[1]}')


# listan läpikäynti while, silmukan avulla
iterator = 0 # = kierosmuuttuja
# iterator += 1 the chain below happens
# while 0 < 5:
# while 1 < 5:
# while 2 < 5:
# while 3 < 5:
# while 4 < 5:

while iterator < len(names): #listan koko
    print(f'Moi {names[iterator]} ikäsi {ages[iterator]}')
    iterator += 1

#names = ['Ville', 'Liisa', 'Mina', 'Fesse', 'MIa']
#ages = [age1, age2, age3, 34, 23]

names = ['Ville', 'Liisa', 'Mina', 'Fesse', 'MIa']
print(names[2:5]) # otetaan 2, 3, 4 (ei viimeistä alkiota), 3 alkiota, indeksistä 2 alkaen
print(names[2:1]) # kaikki loputkin alkiot indeksiltä 2 alkaen
print(names[-1]) #listan viimeinen alkio

print(names[-1:-3:-1]) # wtf the last (-) number is montako numeron välein (esim. -2 = kahden numeron välein)

# listaan voi yhdistää ja siellä voi olla erilaisia tietorakenteita

Lista = ['Mina', 'Fesse', 'Mia']
yhdistetty_Lista = [16, 15, 19, Lista]
print(yhdistetty_Lista)
print(yhdistetty_Lista[3][0]) #sheeeeeeesh

print('\n---------------')

Lista.append('Uusi nimi') # uusi alkio listan loppuun
print(Lista)
Lista.remove('Uusi nimi') # poistetaan alkio, mikäli se löytyy, muuten VIRHE
print(Lista)
if 'Fesse' in Lista:
    print('Fesse löytyi listasta! Ja nyt poistetaan samalla.')
    Lista.remove('Fesse')
    print(Lista)
    Lista.insert(0, 'Fesse')
    print(Lista)

# montenako lisätty nimi nyt oikein on
print(Lista.index('Mina'))

Lisää_nimiä = ['Hannah', 'Mia2', 'Rouie']
Lista.extend(Lisää_nimiä) # lisätään nimet listan perään
print(Lista)

uusi_Lista = Lista + Lisää_nimiä
print(Lista)

Lista[4] = 'Friendo' # muoktaan olemassa olevaa alkiota
print(Lista)

uusi_lista = ['Fesse', 'Mina', 'Mia', 'Hannah', 'Friendo', 'Rouie']
(Lista.sort())
print(uusi_lista)

nimet = []

for kirjain in 'abcde':
    print(kirjain)

for alkio in [1, 2, 3, 4, 5, 6]:
    print(alkio)

for nimi in Lista:
    print(nimi)

for numero in range(5, 50):
    print(numero)

for numero in range(5, 50,2): # hypätään 2 numeron välein because of the number 2 in sulut
    print(numero)

for i in range(999, 8, -3):
    print(i)



# kätetään edellä olevia iteroimaan nimilistaa läpi
# for silmukkia iteraattorille

print(Lista)
for i in range(5): # 1, 2, 3, 4
    print(i)
    print(f'Terve: {Lista[i]}')

print('--------------')
print('Listan potuus rangena')

Listan_pituus = len(Lista)
print(f'Lista on {Listan_pituus} alkiota pitkä')

for i in range(Listan_pituus): # 1, 2, 3, 4
    print(f'Terve: {Lista[i]}')