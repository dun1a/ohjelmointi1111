import mysql.connector
#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
airport = {"EFHK": "Helsinki",
           "BGW": "Bagdad",
           "LHR": "London",
           "RKSI": "Seol"}

while True:
    user_input = input('Mitä haluat: ')
    if user_input == '1':
        ICAO= input('Anna ICAO: ')
        Name= input('Anna nimi: ')
        airport[ICAO]=Name

    elif user_input == '2':
        ICAO= input('Anna ICAO: ')
        print(airport[ICAO])

    elif user_input == '':
        print('Lopetetaan')
        break





