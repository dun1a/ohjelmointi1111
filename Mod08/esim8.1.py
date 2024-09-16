import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', # localhost
         port= 3306,
         database='lentopeli',
         user='root',
         password='w0nn1e205',
         autocommit=True,
         collation = 'utf8mb4_general_ci'
         )
def fetch_airport_by_icao(code):
    sql = (f"select name, municipality from airport where ident = '{code}'")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    # palauttaa monikon, paitsi jos tyhjä tulosjoukko -> tulostaa None
    print(result_row)
    return result_row

user_input = input('Anna ICAO-koodi: ')
airport = fetch_airport_by_icao(user_input)


# jos airport muuttujassa on jotain muuta kuin None, False tai 0
if airport: # vastaa: airport != None
    print(f'Hauttu lentokenttä: {airport[0]}, {airport[1]}')
else:
    print('Lentokenttä ei löydy annetulla koodilla.')

'''
print('\nEXTRA\n') #tiedon lisäys

def add_airport(icao, name, municipality): #municipality = paikkakunta
    sgl = (f"INSERT INTO airport (id, ident) VALUES (999, '{icao}', '{name}', '{municipality}')")
    cursor = connection.cursor()
    cursor.execute(sgl)

icao = input('Anna uusi ICAO: ')
name = input('Anna uusi kentän nimi: ')
municipality = input('Ja paikkakunta: ')
add_airport(icao, name, municipality)
'''

