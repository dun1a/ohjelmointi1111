
def listan_summa(kokonaisluvut):
    #print('Sinulla on seuraavat kokonaisluvut listassasi: ')
    summa = 0
    for i in kokonaisluvut:
        print(i)
        summa += i
    return summa

kokonaisluvut = [2,4,6,8]
print(listan_summa(kokonaisluvut))



