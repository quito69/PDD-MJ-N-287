import csv

with open('peliculas.csv', encoding='utf-8') as archivo_in, open('peliculas_salida2.csv', 'w', newlin='', encoding='utf-8') as archivo_out:
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out, delimiter=';')
    salida.writerow(['Director', 'Año', 'Pelicula'])


for linea in entrada:
   salida.writerow([lista[2], lista[1], lista[0]])

