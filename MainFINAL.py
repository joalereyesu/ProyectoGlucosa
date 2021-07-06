import pandas as pd
import os
from datetime import datetime
import Functions

db = pd.read_excel('Glucosa-Project.xlsx')
database = db.dropna()

opcion = 0
hora_med = input("Ingrese la hora de su medicamento (HH:MM): ")
decimal_time = []
time = []
glucosa = []
condicion = []

while (opcion != 9):
    print("MENU\n\n 1. Rango de Analisis\n 2. Graficas\n 3. Tabla de metabolizacion de Glucosa\n 4. Aceleracion metabolica de la glucos \n 5. Glucosa Promedio\n 6. Glucosa-meta\n 7. Tendencia\n 8. Resumen Estadistico\n")
    opcion = int(input("Ingrese una opcion: "))
    if (opcion == 1):
        fecha_inicial = input("Ingrese la fecha de inicio de la muestra (yyyy-mm-dd): ")
        fecha_final = input("Ingrese la fecha final de la muestra (yyyy-mm-dd): ")
        (decimal_time, time, glucosa, condicion) = Functions.getPoints(database, fecha_inicial, fecha_final)
        print(decimal_time)
        print(time)
        print(glucosa)
        print(condicion)
            
    if opcion == 3:
        print("TABLA DE METABOLIZACION DE GLUCOSA\n")
        razon_cambio = Functions.RazonCambio(decimal_time, glucosa)
        print(razon_cambio)
        print("No.      Tiempo      Glucosa      Razon de Cambio       Condicion\n")
        print("---------------------------------------------------------------------")
        for i in range(len(razon_cambio)):
            print(f"{i}      {time[i]}      {glucosa[i]}      {razon_cambio[i]}      {condicion[i]}")
        print("---------------------------------------------------------------------")
    
    if opcion == 4:
        

