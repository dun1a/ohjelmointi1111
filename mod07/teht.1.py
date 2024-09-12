# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kuukaudet = ('Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu')

kuukausi_num = int(input('Anna kuukauden numero (1-12): '))

if kuukausi_num in (12, 1, 2):
    vuodenaika = 'kuukausi kuuluu vuodenaikaan Talvi'
    print(vuodenaika)
elif kuukausi_num in (3, 4, 5):
    vuodenaika = 'kuukausi kuuluu vuodenaikaan Kevat'
    print(vuodenaika)
elif kuukausi_num in (6, 7, 8):
    vuodenaika = 'kuukausi kuuluu vuodenaikaan Kesa'
    print(vuodenaika)
elif kuukausi_num in (9, 10, 11):
    vuodenaika = 'kuukausi kuuluu vuodanaikaan Syksy'
    print(vuodenaika)










