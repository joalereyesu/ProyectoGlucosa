import pandas as pd
import os
from datetime import datetime
import Functions
import matplotlib.pyplot as plt
import numpy
import pylab

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
            
    if (opcion == 2):
        op=int(input('¿Cómo desea visualizar la gráfica?\n1.Puntos\n2.Curva generada por Polinomio\n'))
        if op == 1:
            plt.scatter(decimal_time, glucosa)
            z = numpy.polyfit(decimal_time, glucosa, 1)
            p = numpy.poly1d(z)
            pylab.plot(decimal_time,p(decimal_time),"r--")
            plt.title('Niveles de Glucosa en Base al Tiempo')
            plt.xlabel('Horas en decimales')
            plt.ylabel('Niveles de glucosa')
            plt.show()
        if op == 2:
            yinters=[]
            for i in range(len(decimal_time)):
                Yinter=Functions.LagrangePol(decimal_time, glucosa, decimal_time[i])
                yinters.append(Yinter)
            print(yinters)
            plt.plot(decimal_time, yinters)
            plt.title('Niveles de Glucosa en Base al Tiempo')
            plt.xlabel('Horas en decimales')
            plt.ylabel('Niveles de glucosa')
            plt.show()
            
            


    if opcion == 3:
        print("TABLA DE METABOLIZACION DE GLUCOSA\n")
        razon_cambio = Functions.RazonCambio(decimal_time, glucosa)
        print("No.      Tiempo      Glucosa      Razon de Cambio       Condicion\n")
        print("---------------------------------------------------------------------")
        for i in range(len(razon_cambio)):
            print(f"{i}      {time[i]}      {glucosa[i]}      {razon_cambio[i]}      {condicion[i]}")
        print("---------------------------------------------------------------------")
    
    if opcion == 4:
        print("ACELERACION METABOLICA DE LA GLUCOSA\n")
        acel = Functions.Aceleracion(decimal_time, glucosa)
        print(f"Aceleracion minima metabolica de la glucosa: {min(acel)}")
        print(f"Aceleracion maxima metabolica de la glucosa: {max(acel)}")

