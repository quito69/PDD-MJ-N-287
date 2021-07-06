import csv
import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base006',
                                   user = 'pdp_usuario006',
                                   password = 'eantpass')
cursor = conexion.cursor()

bares = '''CREATE TABLE IF NOT EXISTS baresbsas ( 
       id INT(20) NOT NULL AUTO_INCREMENT,
       nombre VARCHAR(50) NULL,
       direccion VARCHAR(50) NULL,
       comuna VARCHAR(50) NULL,
       PRIMARY KEY (id))
       ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;;'''
    
cursor.execute(bares)
    
#with open('oferta_gastronomica.csv', encoding='utf-8') as archivo_in:
archivo_in = open('oferta_gastronomica.csv', encoding='utf-8')
entrada = csv.reader(archivo_in)    

next(entrada)

for linea in entrada:
#    print( linea[3], linea[13], linea[15] ) 
    nombre = linea[3]
    direccion = linea[13]
    comuna = linea[15]
    
    q = """ INSERT INTO baresbsas ( nombre, direccion, comuna ) 
        values (%s,%s,%s)     
    """ 
        
    cursor.execute(q, (nombre, direccion, comuna))

conexion.commit()

archivo_in.close()

cursor.close()
conexion.close()