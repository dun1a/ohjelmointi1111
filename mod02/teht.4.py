# kysytään 3 kokonaislukua, plussataan, kerrotaan


eka = int(input("Anna eka kokonaisluku: "))
toka = int(input("Anna toka kokonaisluku: "))
kolmas = int(input("Anna kolmas kokonaisluku: "))

summa = (eka + toka + kolmas)
# print(summa)
tulo = (eka * toka * kolmas)
# print(tulo)
keskiarvo =(summa / 3) # keskiarvo lasketaan
# print(keskiarvo)

print(f"Kolmen kokonaisluvun summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo:.1f}.")

