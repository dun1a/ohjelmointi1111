class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkalainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        # ei kannata kirjoittaa tätä nöin, mutta se toimii silti print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")
        super().tulosta_tiedot()
        print(f"Tuntipalkkalaisen palkka: {self.tuntipalkka}")

class Kuukausipalkkalainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkkalainen):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkkalainen

    def tulosta_tiedot(self):
        # ei kannata kirjoittaa tätä nöin, mutta se toimii silti print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")
        super().tulosta_tiedot()
        print(f"Kuukausipalkkailaisen palkka: {self.kuukausipalkka}")

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
työntekijät.append(Tuntipalkkalainen('Menes', 'Ahmed', 500))
työntekijät.append(Kuukausipalkkalainen('Fesse', 'Ahmed', 90000))

for t in työntekijät:
    t.tulosta_tiedot()

