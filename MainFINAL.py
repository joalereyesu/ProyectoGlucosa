import pandas as pd #Sirve para abrir el Excel, es un data frame
import os 
from datetime import datetime
import Functions
import matplotlib.pyplot as plt #para graficar
import numpy as np, numpy #para graficar
import pylab #para graficar

db = pd.read_excel('Glucosa-Project.xlsx') #Comando para abrir la base de datos en Excel
database = db.dropna() #Depura la base de datos

opcion = 0 #inicializamos el menú
hora_med = input("Ingrese la hora de su medicamento (HH:MM): ") #Guarda la hora ingresada por el ususario
decimal_time = [] 
time = []
glucosa = []
condicion = []
fechas = []

while (opcion != 9):
    print("MENU\n\n 1. Rango de Analisis\n 2. Graficas\n 3. Tabla de metabolizacion de Glucosa\n 4. Aceleracion metabolica de la glucos \n 5. Glucosa Promedio\n 6. Glucosa-meta\n 7. Tendencia\n 8. Resumen Estadistico\n 9. Salir")
    opcion = int(input("Ingrese una opcion: ")) #Muestra todas las opciones del menú
    if (opcion == 1): #Toma el rango de fechas
        print("Recuerde que las fechas ingresadas deben estar en la base de datos sino el programa no funcionara.\n")
        fecha_inicial = input("Ingrese la fecha de inicio de la muestra (yyyy-mm-dd): ")
        fecha_final = input("Ingrese la fecha final de la muestra (yyyy-mm-dd): ")
        (decimal_time, time, glucosa, condicion, fechas) = Functions.getPoints(database, fecha_inicial, fecha_final) #Se va a la función 'getpoints' que toma un rango de fechas y verifica que no se repita la misma hora y que la muestra sea menor o igual a 10
        #Imprime en una tabla todo el rango de fechas
        print("\n                     MUESTRA SELECCIONADA")
        print("---------------------------------------------------------------------")
        print("No.           Fecha               Hora      Glucosa    Condicion")
        print("---------------------------------------------------------------------")
        for i in range(len(time)):
            print(f"{i}      {fechas[i]}      {time[i]}      {glucosa[i]}         {condicion[i]}")
        print("---------------------------------------------------------------------")
        enter = input("Presione enter para continuar: ")

    if (opcion == 2): #
        op=int(input('¿Cómo desea visualizar la gráfica?\n1.Puntos\n2.Curva generada por Polinomio\n'))
        if op == 1: #Este 'if' sirve para imprimir la gráfica con puntos
            plt.scatter(decimal_time, glucosa)
            z = numpy.polyfit(decimal_time, glucosa, 1) #utilizado para calcular trendline
            p = numpy.poly1d(z) #utilizado para calcular trendline
            pylab.plot(decimal_time,p(decimal_time),"r--") #utilizado para calcular trendline
            plt.title('Niveles de Glucosa en Base al Tiempo') 
            plt.xlabel('Horas en decimales')
            plt.ylabel('Niveles de glucosa')
            plt.show()
        if op == 2: #Genera la gráfica en base al polinomio interpolante de Lagrange
            yinters=[]
            for i in range (len(decimal_time)): #Manda a llamar los valores, los guarda en un array y después los grafica
                yinter=Functions.LagrangePol(decimal_time,glucosa,decimal_time[i])
                yinters.append(yinter)
            plt.plot(decimal_time, yinters)
            plt.title('Niveles de Glucosa en Base al Tiempo')
            plt.xlabel('Horas en decimales')
            plt.ylabel('Niveles de glucosa')
            plt.show()
        enter = input("Presione enter para continuar: ")
        
    if opcion == 3: #Se hace la razón de cambio, que es la primera derivada
        print("TABLA DE METABOLIZACION DE GLUCOSA\n")
        razon_cambio = Functions.RazonCambio(decimal_time, glucosa) #Aqui se manda a llamar una función que calcula la primera derivada
        #Imprime la info en una tabla
        print("No.      Hora      Glucosa      Razon de Cambio       Condicion\n")
        print("---------------------------------------------------------------------")
        for i in range(len(razon_cambio)):
            print(f"{i}      {time[i]}      {glucosa[i]}      {razon_cambio[i]}      {condicion[i]}")
        print("---------------------------------------------------------------------")
        enter = input("Presione enter para continuar: ")

    if opcion == 4: # Se utiliza la función 'aceleración' que calcula la segunda derivada
        print("ACELERACION METABOLICA DE LA GLUCOSA\n")
        acel = Functions.Aceleracion(decimal_time, glucosa)
        print(f"Aceleracion minima metabolica de la glucosa: {min(acel)}") 
        print(f"Aceleracion maxima metabolica de la glucosa: {max(acel)}")
        enter = input("Presione enter para continuar: ")

    if opcion == 5: 
        print('GLUCOSA PROMEDIO POR LAS FECHAS ESCOGIDAS\n')
        n=1/(len(decimal_time)-2) #En esta se calcula la glucosa promedio usando la integral
        a=Functions.Trapecio(decimal_time, glucosa) # Se utiliza la regla de integración por trapecio
        promedio=n*a #Se calcula el promedio
        print(f"La glucosa promedio en esas fechas es: {promedio}")
        enter = input("Presione enter para continuar: ")
    
    if opcion == 6: #Se busca aproximar a qué hora tendrá el nivel de glucosa ingresado
        inp_gluc = int(input("Ingrese el valor especifico de nivel de glucosa: "))
        (mod_gluc, mod_time) = Functions.checkforduplicates(glucosa, decima_time)
        tiempo_calc = Functions.LagrangePol(mod_gluc, mod_time, inp_gluc)
        (h, m) = Functions.makeTime(tiempo_calc)
        print("Hora: %d:%02d" % (h, m))
        enter = input("Presione enter para continuar: ")

    if opcion == 7: #Se usa regresión lineal para obtener el coef. de determinación 
        print("TENDENCIAS\n")
        r2 = Functions.RegLin(decimal_time, glucosa) #Se utiliza la función de regresión lineal con el arreglo de las hrs y la glucosa
        print(f"El coeficiente de determinacion: {r2}") 
        enter = input("Presione enter para continuar: ")

    if opcion == 8: #Aquí se hace el resumen estadístico
        vals=np.sort(glucosa) #se ordenan: menor->mayor
        gluc=np.array(vals) #se convierte en un arreglo que pueda usar numpy
        media=np.mean(gluc) #saca la media
        mediana=np.median(gluc) #se calcula la mediana
        maximo=max(gluc) #se calcula el valor max
        minimo=min(gluc) #se calcula el valor min
        desviacion=np.std(gluc) #se calcula la desv. estándar
        # Se imprime toda la información en una tabla
        print('  MEDIA         MEDIANA           VALOR MÁXIMO         VALOR MÍNIMO      DESVIACIÓN ESTÁNDAR\n')
        print('______________________________________________________________________________________________\n')
        print(f'  {media}          {mediana}             {maximo}               {minimo}           {desviacion}\n')
        print('______________________________________________________________________________________________\n')
    
        plt.hist(vals, bins=len(vals-1)) #Se genera un histograma con los datos
        plt.xlabel('Glucosa')
        plt.ylabel('Frecuencia')
        plt.show() #imprime la gráfica
        enter = input("Presione enter para continuar: ")