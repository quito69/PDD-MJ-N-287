import mysql.connector
import csv

def insert_bar_mysql(conn, tup):
    cursor = conn.cursor()
    query = "INSERT INTO bares (nombre, direccion, comuna) values(%s,%s,%s)"
    try:
        cursor.executemany(query, tup)
        conn.commit()
    except:
        conn.rollback()

    cursor.close()
    

with open('oferta_gastronomica.csv', encoding='utf-8') as archivo_in: 
    entrada = csv.reader(archivo_in)
    next(entrada)

    conexion = mysql.connector.connect(host= 'cloud.eant.tech', database = 'pdp_base006', user = 'pdp_usuario006', password = 'eantpass')



    tupBar = [] 
    for linea in entrada:

        tupBar.append((
            linea[3],
            linea[13],
            linea[15]
        )) #append data


    insert_bar_mysql(conexion, tupBar)


conexion.close()

