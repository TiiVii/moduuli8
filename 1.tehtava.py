import mysql.connector

def koodilla(ident):
    sql = 'SELECT name, municipality FROM airport'
    sql += " WHERE ident='"+ident+"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f'Lentoasema {rivi[0]} sijaitsee kunnassa nimelta {rivi[1]}.')
    return


yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'fl1ght_game',
    user = 'root',
    password = 'vaahtokarkki',
    autocommit = True
)

ident = input('Anna lentoaseman ICAO-koodi: ')

koodilla(ident)