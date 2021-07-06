archivo_in = open('hospitales.csv', encoding='utf-8')
archivo_out = open('hospitales_ordenados2.csv', 'w', encoding='utf-8')

titulo = ','.join(['Latitud', 'Longitud', 'Dirección', 'Hospital'])
archivo_out.write(titulo + '\n')


for linea in archivo_in:
    linea = str.replace(linea, '"', '')
    linea = linea.strip('\n')
    lista = linea.split(',')

    auxlat = str.find(lista[0], '58.')
    if auxlat != -1:
       auxlon = str.find(lista[0], '34.')
       aux = str.find(lista[0], ')')
       
       latitud = linea[auxlat : auxlon-2]
       longitud = linea[auxlon : aux]

       unidos = ','.join([latitud, longitud, lista[5]+' '+lista[6], lista[2]])
       archivo_out.write(unidos + '\n')

       
archivo_in.close()
archivo_out.close()    