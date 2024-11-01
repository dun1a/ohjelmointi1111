class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.odometer = 0

    def set_nopeus(self, nopeus):
        self.nopeus = min(nopeus, self.huippunopeus)

    def aja(self, tunnit):
        etaisyys = self.nopeus * tunnit
        return etaisyys

class Sahkoauto(Auto):
    def __init__(self, rek_nro, huippunopeus, akkukapasiteetti):
        super().__init__(rek_nro, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottori(Auto):
    def __init__(self, rek_nro, huippunopeus, bensastankki):
        super().__init__(rek_nro, huippunopeus)
        self.bensastankki = bensastankki

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
sahkoauto.set_nopeus(120)

polttomoottoriauto = Polttomoottori("ABC-123", 165, 32.3)
polttomoottoriauto.set_nopeus(110)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print(f"{sahkoauto.rek_nro} sähköauto - etäisyys: {sahkoauto.odometer} km")
print(f"{polttomoottoriauto.rek_nro} polttomoottoriauto - etöisyys: {polttomoottoriauto.odometer} km")
