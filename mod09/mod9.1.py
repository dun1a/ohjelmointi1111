# tehtävä

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0

    def printtaa_ominaisuudet(self):
        print(f'Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus on {self.huippunopeus}.')

auto = Auto("ABC-123",'142 km/h')

auto.printtaa_ominaisuudet()

'''
# maybe teht 3 kuljettaja osa (not needed in teht 2)
class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

# teht 2 (?)
class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.huippunopeus = huippunopeus

    def tulosta(self):
        print(f'Auton rekisteritunnus on {self.rek_nro} ja huppunopeua on {self.huippunopeus}.')
        print(f'tämän hetkinen nopeus on {self.nopeus}.')

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        # rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0


a1 = Auto("ABC-123", 142) #.tulosta()
a2 = Auto("CBA-321", 204)
kuski = Kuljettaja("Räikkönen", 44, a1)

a2.kiihdyta(5)
print(a2.nopeus)
a2.kiihdyta(300)
a1.kiihdyta(-54)
a1.tulosta()
a2.tulosta()


# print(f'{a1.rek_nro}, huippunopeus: {a1.huippunopeus}')

# 
# saman oilioon voidaan viitata useasta muuttujasta
a1 = a2
a1.tulosta()
a2.tulosta()
'''



