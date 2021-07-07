import pandas as pd
import os
from datetime import datetime
import Functions
import matplotlib.pyplot as plt
import numpy as np, numpy
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
    print("MENU\n\n 1. Rango de Analisis\n 2. Graficas\n 3. Tabla de metabolizacion de Glucosa\n 4. Aceleracion metabolica de la glucos \n 5. Glucosa Promedio\n 6. Glucosa-meta\n 7. Tendencia\n 8. Resumen Estadistico\n 9. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if (opcion == 1):
        fecha_inicial = input("Ingrese la fecha de inicio de la muestra (yyyy-mm-dd): ")
        fecha_final = input("Ingrese la fecha final de la muestra (yyyy-mm-dd): ")
        (decimal_time, time, glucosa, condicion) = Functions.getPoints(database, fecha_inicial, fecha_final)


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
            for i in range (len(decimal_time)): 
                yinter=Functions.LagrangePol(decimal_time,glucosa,decimal_time[i])
                yinters.append(yinter)
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

    if opcion == 5:
        print('GLUCOSA PROMEDIO POR LAS FECHAS ESCOGIDAS\n')
        n=1/(len(decimal_time)-2)
        a=Functions.Trapecio(decimal_time, glucosa)
        promedio=n*a
        print(f"La glucosa promedio en esas fechas es: {promedio}")
    if opcion == 6:
        inp_gluc = int(input("Ingrese el valor especifico de nivel de glucosa: "))
        tiempo_calc = Functions.LagrangePol(glucosa, decimal_time, inp_gluc)
        (h, m) = Functions.makeTime(tiempo_calc)
        print("Hora: %d:%02d" % (h, m))

    if opcion == 7:
        print("TENDENCIAS\n")
        r2 = Functions.RegLin(decimal_time, glucosa)
        print(f"El coeficiente de determinacion: {r2}") 

    if opcion == 8:
        vals=np.sort(glucosa)
        gluc=np.array(vals) 
        media=np.mean(gluc)
        mediana=np.median(gluc)
        maximo=max(gluc)
        minimo=min(gluc)
        desviacion=np.std(gluc)
        print('  MEDIA         MEDIANA           VALOR MÁXIMO         VALOR MÍNIMO      DESVIACIÓN ESTÁNDAR\n')
        print('______________________________________________________________________________________________\n')
        print(f'  {media}          {mediana}             {maximo}               {minimo}           {desviacion}\n')
        print('______________________________________________________________________________________________\n')
        plt.hist(vals, bins=len(vals-1))
        plt.xlabel('Glucosa')
        plt.ylabel('Frecuencia')
        plt.show()




