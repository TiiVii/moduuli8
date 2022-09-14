import mysql.connector
from geopy import distance

def kentatkuntoon(maakoodi1, maakoodi2):
    sql = f'''select latitude_deg, longitude_deg
    from airport;'''
    sql += " Where ident = '"+maakoodi1+"' and ident = '"+maakoodi2+"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        ensimmainen = (tulos[0][0], tulos[0][1])
        toinen = (tulos[1][0], tulos[1][1])
        print(f'Lentokenttien etaisyys on: {distance.distance(ensimmainen, toinen).km:.2f}km')



yhteys = mysql.connector.connect(
    host ='localhost',
    port = 3306,
    database = 'fl1ght_game',
    user = 'root',
    password = 'vaahtokarkki',
    autocommit = True
)

maakoodi1 = input('Anna ensimmainen maakoodi: ')
maakoodi2 = input('Anna toinen maakoodi: ')
kentatkuntoon(maakoodi1, maakoodi2)
