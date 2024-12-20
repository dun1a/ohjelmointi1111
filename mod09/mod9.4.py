import random

class Autotalli:
    def __init__(self):
        self.autot = set()
    def auto_sisaan(self, auto):
        for a in self.autot:
            if a == auto:
                return
        self.autot.add(auto)

    def auto_ulos(self, auto):
        self.autot.remove(auto)

    def tulosta_inventaario(self):
        print('Autot tallissa:')
        for auto in self.autot:
            auto.auton_ominaisuudet()

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def auton_ominaisuudet(self):
            print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
            print(f"Nopeus: {self.nopeus}, matkamittari: {self.kuljettu_matka}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        # rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti=0):
            # aika tunneissa
        self.kuljettu_matka += tunti * self.nopeus
        while True:
            for auto in autot:
                nopeuden_muutos = random.randint(-10, 15)
                auto.kiihdyta(nopeuden_muutos)
                auto.kulje(1)
            if self.kuljettu_matka >= 10000:
                break
            tunti += 1

autot = set()
for i in range(10):
    rek_nro = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rek_nro, huippunopeus)
    autot.add(uusi_auto)
'''
tunti = 0 
while True:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
    if any(kuljettu_matka >= 10000 for auto in autot):
        
            return print(f'rekisteri numero {self.rek_nro} on saavuttanut vähintään 1000 km/h')

'''
ominaisuudet = ['Rekisteritunnus', ' Huippunopeus', 'Nopeus', 'kuljettu matka']
table = [auto.auton_ominaisuudet() for auto in autot]
print('Kilpailun tuokset')
print(tabulate(table, headers=ominaisuudet, tablefmt = "grid"))


'''
talli = Autotalli()
talli.auto_sisaan(a1)

#luotaan 10 erilaista auto_oliota autotalliin
for i in range (10):
    uusi_auto = Auto(f"ABC-{i+1}", random.randint(100,200))
    talli.auto_sisaan(uusi_auto)

# a1.kiihdyta(random.randint(-10,15))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for a in self.autot:
        nopeuden_muutos = random.randint(-10,15)
        a.kiihdyta(nopeuden_muutos)
        a.kulje(1)

#a1.kiihdyta()
a1.kulje(1)
talli.tulosta_inventaario()
a1.auton_ominaisuudet()
'''