
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        # nykyinen kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += + 1
        print(f'Hissi on nyt kerroksessa {self.nykyinen_kerros}')

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f'Hissi on nyt kerroksessa {self.nykyinen_kerros}')

    def siirry_kerrokseen(self, kohdekerros):
        print(f'siirretään hissi kerrokseen {kohdekerros}')
        if kohdekerros > self.nykyinen_kerros:
            # olion omia metodeita kutsuttuaessaa kätetään self.
            while kohdekerros > self.nykyinen_kerros:
                self.kerros_ylos()
        elif kohdekerros < self.nykyinen_kerros:
                self.kerros_alas()
        print(f'Hissi on nyt kerroksessa {kohdekerros}')


h = Hissi(1,10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin_kerros)

