import csv
import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base006',
                                   user = 'pdp_usuario006',
                                   password = 'eantpass')
cursor = conexion.cursor()

bares = '''CREATE TABLE IF NOT EXISTS prueba2 ( 
       id INT(20) NOT NULL AUTO_INCREMENT,
       nombre VARCHAR(50) NULL,
       direccion VARCHAR(50) NULL,
       comuna VARCHAR(50) NULL,
       PRIMARY KEY (id))
       ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;;'''
    
cursor.execute(bares)
    
archivo_in = open('oferta_gastronomica.csv', encoding='utf-8')
entrada = csv.reader(archivo_in)    

next(entrada)

lista = [tuple((linea[3], linea[13], linea[15])) for linea in entrada]

'''
lista = []

for linea in entrada:

    lista.append(tuple((linea[3], linea[13], linea[15])))
'''

        
query = """ INSERT INTO prueba2 ( nombre, direccion, comuna ) 
        values (%s, %s, %s)     
    """ 
'''        
try:
    cursor.executemany(query, lista)
    conexion.commit()
except:
    conexion.rollback()
'''    
cursor.executemany(query, lista)

conexion.commit()

    
archivo_in.close()

cursor.close()
conexion.close()




