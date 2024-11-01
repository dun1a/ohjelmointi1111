
class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Julkaisun nimi: {self.nimi}.')

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        # hae nimi yläluokasta
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjan nimi on {kirja.nimi}, kirjoittaja on {kirja.kirjoittaja} ja kirjassa on {kirja.sivumaara} sivua.')

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjan nimi on {l.nimi}, päätoimittaja on {l.paatoimittaja}.')

#j = Julkaisu('Heavenly jäbät')
#print(j.nimi)

kirja = Kirja('Hytti n:o 6', 'Rosa Liksom',  200)
#print(f'Kirjan nimi on {kirja.nimi}, kirjoittaja on {kirja.kirjoittaja} ja kirjassa on {kirja.sivumaara} sivua.')
kirja.tulosta_tiedot()
l = Lehti('Aku Ankka', 'Aki Hyyppä')
l.tulosta_tiedot()