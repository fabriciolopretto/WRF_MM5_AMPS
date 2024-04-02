"""
Descaarga los archivos grib de la corrida del modelo
numérico MM5 WRF-AMPS e su resolución de 3 Km.
"""

# Se importan las librerías necesarias
import requests
import os
import glob
import datetime


# Se captura la fecha y hora
time = datetime.datetime.utcnow()
anno_real = int(time.year)
mes_real = int(time.month)
dia_real = int(time.day)
hora_real = int(time.hour)

# Se define la corrida del modelo
# Anno
anno_tex = str(anno_real)
# Mes
if 10 > mes_real >= 1:
    mes_tex = '0' + str(mes_real)
if mes_real >= 10:
    mes_tex = str(mes_real)
# Dia
if 10 > dia_real >= 1:
    dia_tex = '0' + str(dia_real)
if dia_real >= 10:
    dia_tex = str(dia_real)
# Inicializacion   
if 0 <= hora_real < 12:
    hora_tex = '00'
if 12 <= hora_real <= 23:
   hora_tex = '12'

del time,anno_real,mes_real,dia_real,hora_real


# Define la ruta del script relativa al usuario
ruta = os.path.dirname((os.path.abspath(__file__)))
# limpia la carpeta de destino de corridas anteriores
# Archivos horarios e integrados
files = glob.glob(ruta + '/Archivos/*.grb')
for f in files:
    os.remove(f)
del files


#Creamos el camino de los archivos
for i in range(40):
    if 10 > i >= 0:
        plazo = '00' + str(i)
    if 100 > i >= 10:
        plazo = '0' + str(i)
    downloadURL = 'https://www2.mmm.ucar.edu/rt/amps/wrf_grib/'+ anno_tex + mes_tex + dia_tex + hora_tex +'/'+ anno_tex + mes_tex + dia_tex + hora_tex +'_WRF_d6_f'+ plazo +'.grb'
    req = requests.get(downloadURL)
    filename = req.url[downloadURL.rfind('/')+1:]
    #Descargamos el archivo vigente
    with open(ruta + '/Archivos/'+ filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    del plazo,downloadURL,req,filename,chunk
