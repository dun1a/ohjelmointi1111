# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Kuljettaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def kulje(self, tunnit):
        print(f'Olen {self.nimi}, {self.ika}.')
        self.auto.kiihdyta(30)
        print(self.auto.nopeus)
        self.auto.kulje(1.5)
        self.auto.kiihdyta(70)
        print(self.auto.nopeus)
        self.auto.kulje(1.5)
        self.auto.kiihdyta(-200)
        print(self.auto.nopeus)
        self.auto.kulje(1.5)

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = kuljettu_matka

    def aunton_ominaisuudet(self):
        print(f'Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus on {self.huippunopeus}, hetkellinen nopeus on {self.nopeus} ja matka on {self.kuljettu_matka}')

    def kiihdyta(self, muutettunopeus):
        self.nopeus = self.nopeus + muutettunopeus
        # auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0
        # rajoitetaan kiihdystyksen tulos huippunopeuteen
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus


a1 = Auto("ABC-123",142, 60)
k = Kuljettaja("Mikko", 40)

k.auto()
'''
a.kiihdyta(30)
a.aunton_ominaisuudet()

a.kiihdyta(70)
a.aunton_ominaisuudet()

a.kiihdyta(50)
a.aunton_ominaisuudet()

a.kiihdyta(-200)
a.aunton_ominaisuudet()
'''
'''
a.nopeus = 60
a.kulje(60)
a.kuljettu_matka = 2000
a.kulje(1.5)
print(f'Auton kuljettu matka on {a.kuljettu_matka}')
'''