
def list(kokonaisluvut):
    toinen_lista = [x for x in kokonaisluvut if x % 2 == 0]
    #for i in kokonaisluvut:
     #   print(i)
    return toinen_lista


kokonaisluvut = [1, 2, 3, 4, 5, 6, 7, 9, 12]
print(kokonaisluvut)
print(list(kokonaisluvut))


