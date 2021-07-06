
# Formato de Fecha 'DD-MM-AAAA'

from datetime import datetime


def normalizadorFechas(fecha, patron_in, patron_out = "%d-%m-%Y"):
   objeto_fecha = datetime.strptime(fecha, patron_in)
   fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
   return fecha_normalizada

def traductorFecha(fecha):
   meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO', 'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
   lista = fecha.split(' de ')
   mes = lista[1].upper()
   nro_mes = meses.index(mes) + 1
   fecha_aux = lista[0] + '-' + str(nro_mes) + '-' + lista[2]
   return fecha_aux


import csv

archivo_in = open('reclamos.csv', encoding='ANSI')
tabla = csv.reader(archivo_in)
archivo_out = open('reclamos_fecha_ordenada.csv', 'w', encoding='ANSI')

for linea in tabla:
    aux = linea[0]
    aux = str.replace(aux, ';', ',')
    lista = aux.split(',')
    try:
       fecha = normalizadorFechas(lista[3], '%Y-%d-%m')
    except:
        try:
            fecha = normalizadorFechas(lista[3], '%d/%m/%y')
        except:
            try:
                fecha = normalizadorFechas(lista[3], '%d/%m/%Y')
            except:
                try:
                    fecha = normalizadorFechas(lista[3], '%Y-%d-%m')
                except:
                    try:
                        fecha = normalizadorFechas(lista[3], '%d-%m-%Y')
                    except:
                        try:
                           fecha = normalizadorFechas(traductorFecha(lista[3]), '%d-%m-%Y')
                        except:
                           fecha = lista[3]
        
    unidos = ','.join([lista[0], lista[1], lista[2], fecha])
    archivo_out.write(unidos + '\n')

archivo_in.close()
archivo_out.close()

