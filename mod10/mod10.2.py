class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros  # Hissin alin kerros
        self.ylin_kerros = ylin_kerros  # Hissin ylin kerros
        self.nykyinen_kerros = alin_kerros  # Hissi aloittaa alimmasta kerroksesta

    def kerros_ylos(self):
        """Siirtää hissiä yhden kerroksen ylöspäin, jos ei olla ylimmässä kerroksessa."""
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        """Siirtää hissiä yhden kerroksen alaspäin, jos ei olla alimmassa kerroksessa."""
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        """Siirtää hissin haluttuun kerrokseen kutsumalla kerros_ylös- tai kerros_alas-metodia."""
        print(f"Siirretään hissi kerrokseen {kohde_kerros}...")

        # Tarkistetaan, että kohdekerros on hissin sallittujen kerrosten sisällä
        if not (self.alin_kerros <= kohde_kerros <= self.ylin_kerros):
            print("Virhe: Kerros ei ole hissin kulkualueella.")
            return


        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()
        print(f"Hissi on saapunut kerrokseen {kohde_kerros}.")


# Pääohjelma
if __name__ == "__main__":
    # Luodaan hissi, joka liikkuu kerrosten 1 ja 10 välillä
    hissi = Hissi(2, 10)

    # Siirrytään haluttuun kerrokseen, esimerkiksi kerrokseen 5
    hissi.siirry_kerrokseen(5)

    # Siirretään hissi takaisin alimpaan kerrokseen
    hissi.siirry_kerrokseen(hissi.alin_kerros)
