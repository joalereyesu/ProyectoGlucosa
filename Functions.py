import pandas as pd
from datetime import date, datetime
import time
import random
import math
import matplotlib.pyplot as plt
import numpy
import pylab

#Todas las horas las pasa a formato decimal
def makeX(horas):
    tiempo = []
    for hour in horas:
        (h, m, s) = hour.split(':')
        result = int(h) + (int(m)/60)
        tiempo.append(result)
    return tiempo

#Pasa de decimal a formato de hrs
def makeTime(decimal_time):
    hours = int(decimal_time)
    minutes = (decimal_time*60) % 60
    return hours, minutes

def checkforduplicates(lista, lista2):
    res = []
    res2 = []
    for i in range(len(lista)):
        if lista[i] not in res:
            res.append(lista[i])
            res2.append(lista2[i])
    return res, res2

def getPoints(db, di, df):
    horas = []
    rand_horas = []
    glucosa = []
    rand_glucosa = []
    condicion = []
    rand_condicion = []
    fechas = []
    rand_fechas = []
    puntosx = []
    inicio=0
    final=0
    datei = datetime.strptime(di, '%Y-%m-%d') #Se pasa la info a formato DateTime
    datef = datetime.strptime(df, '%Y-%m-%d') #Se pasa la info a formato DateTime
    for index, row in db.iterrows(): #se itera la base de datos
        if row['Fecha'] == datei: #Se verifica que la fecha inicial esté en la columna 'Fecha'
            inicio = index #Es la posición inicial del vector
        if row['Fecha'] == datef: #Se verifica que la fecha final esté en la columna 'Fecha'
            final = index #Es la posición final del vector

    for element in range(inicio, final): #itera entre la posición inicial y la final
        #Se crean diferentes vectores para las variables
        horas.append(str(db.loc[element, 'Hora'])) 
        glucosa.append(int(db.loc[element, 'mg/dL']))
        condicion.append(str(db.loc[element, 'Condición']))
        fechas.append(str(db.loc[element, 'Fecha']))


    if len(horas) <= 10: #Verifica que el largo del vector sea <= 10
        #se crean nuevos vectores para las variables
        horas_updated = []
        glucosa_updated = []
        condicion_updated = []
        fechas_updated = []
        for i in range(len(horas)): #itera el vector horas 
            if horas[i] not in horas_updated: #Verifica que no se repita ningún valor
                #Se actualizan todas las variables para que ninguna se repita
                horas_updated.append(horas[i])
                glucosa_updated.append(glucosa[i])
                condicion_updated.append(condicion[i])
                fechas_updated.append(fechas[i])
        puntosx = makeX(horas_updated) #convierte las horas a formato decimal
        return puntosx, horas_updated, glucosa_updated, condicion_updated, fechas_updated 
    else: #Aquí se usa cuando el largo de la muestra es mayor a 10
        while (len(rand_horas)<10):
            rand_num = random.randint(0, (len(horas)-1)) #Se crea un número random
            #Devuelve un elemento random de cada vector
            element_h = horas[rand_num] 
            element_g = glucosa[rand_num]
            element_c = condicion[rand_num]
            element_f = fechas[rand_num]
            if element_h not in rand_horas: #Verifica que no se repita ningún valor
                #Se guardan todas las variables random en vectores
                rand_horas.append(element_h)
                rand_glucosa.append(element_g)
                rand_condicion.append(element_c)
                rand_fechas.append(element_f)
        puntosx = makeX(rand_horas) #Convierte las horas a formato decimal
        return puntosx, rand_horas, rand_glucosa, rand_condicion, rand_fechas

#Función de primera derivada
def RazonCambio(x, y):
    n = len(x)
    dx = []
    val = (y[1] - y[0])/(x[1] - x[0])
    dx.append(val)
    i = 1
    while i != (n-1):
        val = (y[i+1] - y[i-1])/(x[i+1] - x[i-1])
        dx.append(val)
        i = i + 1
    val =  (y[n-1] - y[n-2])/(x[n-1] - x[n-2])
    dx.append(val)
    return dx

#Función de la segunda derivada
def Aceleracion(x, y):
    dx2 = []
    n = len(x)
    val = (y[0] - 2*y[2] + y[3]) / ((x[2] - x[1])**2); 
    dx2.append(val)
    i = 1
    while i != (n-1):
        val = (y[i-1] - 2*y[i] + y[i+1]) / ((x[i] - x[i-1])**2)
        dx2.append(val)
        i = i + 1
    val = (y[n-3] - 2*y[n-2] + y[n-1]) / ((x[n-1] - x[n-2])**2)
    dx2.append(val)
    return dx2

#Polinomio interpolante utilizando función de Lagrange (lo hicimos en clase)
def LagrangePol(x,y,xint):
    sum=0
    n=len(x)
    for i in range(n):
        producto=y[i]
        for j in range(n):
            if i !=j:
                producto*=((xint-x[j])/(x[i]-x[j]))
        sum+=producto
    Yinter=sum
    return Yinter

#Regresión lineal (lo hicimos en clase)
def RegLin(x, y):
    n = len(x)
    x2 = []
    xy = []
    y2 = []
    if len(y) != n:
        print("Debe haber la misma canitdad de valores para 'x' y 'y'")
    sx = sum(x)
    sy = sum(y)
    for i in range(len(x)):
        x2.append(x[i]*x[i])
        xy.append(x[i]*y[i])
        y2.append(y[i]*y[i])
    sx2 = sum(x2)
    sxy = sum(xy)
    sy2 = sum(y2)
    pendiente = (n*sxy - sx*sy)/(n*sx2 - sx**2)
    intery = sy/n - pendiente * sx/n
    r2 = ((n*sxy - sx*sy)/math.sqrt(n * sx2 - sx**2)/math.sqrt(n*sy2 - sy**2))**2
    xp = numpy.linspace(min(x), max(x), 2)
    yp = pendiente*xp+intery
    plt.scatter(x, y)
    plt.plot(xp, yp)
    plt.show()
    return r2

#Calcula la integral por medio del método del Trapecio (lo hicimos en clase)
def Trapecio(x,y):
    l=len(x)
    h=x[2]-x[1]
    I=(0.5*(y[1]+y[2]))*h
    i=1
    for i in range(l-1):
        h=x[i+1] - x[i]
        I+=(0.5*y[i]+y[i+1])*h
    return I