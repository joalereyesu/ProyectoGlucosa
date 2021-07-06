import pandas as pd
import os
from datetime import datetime
import Functions
import random

db = pd.read_excel('Glucosa-Project.xlsx')
database = db.dropna()

hora_med = input("Ingrese la hora de su medicamento (HH:MM): ")
print("MENU\n\n 1. Rango de Analisis\n 2. Graficas\n 3. Tabla de metabolizacion de Glucosa\n 4. Aceleracion metabolica de la glucos \n 5. Glucosa Promedio\n 6. Glucosa-meta\n 7. Tendencia\n 8. Resumen Estadistico\n")
opcion = int(input("Ingrese una opcion: "))
horas = []
new_horas = []

if (opcion == 1):
    fecha_inicial = input("Ingrese la fecha de inicio de la muestra (yyyy-mm-dd): ")
    fecha_final = input("Ingrese la fecha final de la muestra (yyyy-mm-dd): ")
    datei = datetime.strptime(fecha_inicial, '%Y-%m-%d')
    datef = datetime.strptime(fecha_final, '%Y-%m-%d')
    for index, row in database.iterrows():
        if row['Fecha'] == datei:
            inicio = index
        if row['Fecha'] == datef:
            final = index

    for element in range(inicio, final):
        horas.append(str(db.loc[element, 'Hora']))

    if len(horas) <= 10:
        puntosx = Functions.makeX(horas, hora_med)
    else: 
        while (len(new_horas)<10):
            element = horas[random.randint(0, (len(horas)-1))]
            if element not in new_horas:
                new_horas.append(element)
        puntosx = Functions.makeX(new_horas, hora_med)

        

