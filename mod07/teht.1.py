# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kuukaudet = ('Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu')
kaudet = ('talvi', 'kevät', 'kesä', 'syksy')

kuukausi_num = int(input('Anna kuukauden numero (1-12): '))

kausinum = (kuukausi_num % 12) // 3
kausi = kaudet[kausinum]
print(f'{kuukaudet[kuukausi_num-1]} on {kausi}')












