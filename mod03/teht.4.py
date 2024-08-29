
year = int(input('Anna vuosiluku: '))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): # != tarkoittaa ei ole, ==0 takoittaa jaollinen jollekin
    print('on karkausvuosi.')
else:
    print('ei ole karkausvuosi.') #jos laitettu luku ei ole 4:llä jaollinen
