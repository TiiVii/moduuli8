import mysql.connector

def synkataan(maakoodi):
    sql2 = f'''SELECT airport.type, count(*)
    from airport
    where airport.iso_country = "{maakoodi}"
    group by type;'''
    kursori = yhteys.cursor()
    kursori.execute(sql2)
    tulo2 = kursori.fetchall()
    if kursori.rowcount >0:
        print(f'Maan lentokenttatyypit: \n'
              f'Suljettuja: {tulo2[0][1]}\n'
              f'Heliportteja: {tulo2[1][1]}\n'
              f'Suuret lentokentat: {tulo2[2][1]}\n'
              f'Keskikokoiset lentokentat: {tulo2[3][1]}\n'
              f'Pienet lentokentat: {tulo2[4][1]}')


yhteys = mysql.connector.connect(
    host= 'localhost',
    port = 3306,
    database = 'fl1ght_game',
    user = 'root',
    password = 'vaahtokarkki',
    autocommit = True
)

maakoodi = input('Anna etsimasi maan maakoodi: ')
synkataan(maakoodi.upper())