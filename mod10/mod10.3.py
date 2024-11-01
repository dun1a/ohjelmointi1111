class Talo:
    def __init__(self, alin_ker_num, ylin_ker_num, hissi_maara):
        self.alin_ker_num = alin_ker_num
        self.ylin_ker_num = ylin_ker_num
        self.hissi_maara = [Hissi(alin_ker_num, ylin_ker_num) for i in range(hissi_maara)]

    def aja_hissi(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero <= len(self.hissi_maara):
            print(f'ajetaan hissiä {hissi_numero +1} kerrokseen {kohdekerros}')
            self.hissi_maara[hissi_numero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print('palohälytys! Kaikki hissit menevät ekaan kerrokseen!')
        for hissi in self.hissi_maara:
            hissi.siirry_kerrokseen(self.alin_ker_num)

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

talo = Talo(1, 10, 3)
talo.aja_hissi(0, 5)
talo.palohalytys()