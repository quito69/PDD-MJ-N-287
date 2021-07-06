import csv

with open('hospitales.csv', encoding='utf-8') as archivo_in, open('hospitales_salida.csv', 'w', newline='',  encoding='utf-8') as archivo_out: 
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out, delimiter=';')
    salida.writerow(['Latitud','Longitud', 'Direccion', 'Nombre'])
    
    next(entrada)
    
    for linea in entrada:
        aux = linea[0].split(' ')
        lat = aux[1].replace('(','')
        lon = aux[2].replace(')','')

        salida.writerow([lat, lon, linea[5]+' '+linea[6], linea[2]])
    
                         





