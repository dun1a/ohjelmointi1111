
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        # nykyinen kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            # olion omia metodeita kutsuttuaessaa kätetään self.
            while kohdekerros > self.kerros:
                self.kerros_ylos()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                self.kerros_alas()

    def kerros_ylos(self, kerros):
        if self.kerros < self.ylin_kerros:
            self.kerros += + 1
        print(f'nkyinen kerros on {self.kerros}')

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f'nkyinen kerros on {self.kerros}')


h = Hissi(1,10)
h.siirry_kerrokseen(5)
