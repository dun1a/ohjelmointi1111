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




