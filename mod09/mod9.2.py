
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, hetk_nopeus=0, kuljettu_matka=0):
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


a = Auto("ABC-123",142)

a.kiihdyta(30)
a.aunton_ominaisuudet()

a.kiihdyta(70)
a.aunton_ominaisuudet()

a.kiihdyta(50)
a.aunton_ominaisuudet()

a.kiihdyta(-200)
a.aunton_ominaisuudet()

