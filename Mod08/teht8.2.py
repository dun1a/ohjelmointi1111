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
cursor = connection.cursor()

def hae_lentokenttä_määrä(maakoodi):
    sql = f"select type from airport where iso_country = '{maakoodi}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()

    smallport = medport = largeport = heliport =closedport = 0

    if cursor.rowcount > 0:
        for rivi in result:
            if rivi[0] == 'small_airport':
                smallport +=1
            elif rivi[0] == 'medium_airport':
                medport +=1
            elif rivi[0] == 'large_airport':
                largeport +=1
            elif rivi[0] == 'heliport':
                heliport +=1
            elif rivi[0] == 'colsed':
                closedport +=1


        print(f'Pienet lentokentät:{smallport}')
        print(f'Keksi lentokentät:{medport}')
        print(f'Isot lentäkentät:{largeport}')
        print(f'Helikopteri lentokentät:{heliport}')
        print(f'Suljetut lentokentät:{closedport}')
        return

maakoodi = input('Anna maakoodi: ')
hae_lentokenttä_määrä(maakoodi)
