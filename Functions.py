import pandas as pd
from datetime import date, datetime
import time
import random
import math
import matplotlib.pyplot as plt
import numpy
import pylab

def makeX(horas):
    tiempo = []
    for hour in horas:
        (h, m, s) = hour.split(':')
        result = int(h) + (int(m)/60)
        tiempo.append(result)
    return tiempo

def getPoints(db, di, df):
    horas = []
    rand_horas = []
    glucosa = []
    rand_glucosa = []
    condicion = []
    rand_condicion = []
    puntosx = []
    datei = datetime.strptime(di, '%Y-%m-%d')
    datef = datetime.strptime(df, '%Y-%m-%d')
    for index, row in db.iterrows():
        if row['Fecha'] == datei:
            inicio = index
        if row['Fecha'] == datef:
            final = index

    for element in range(inicio, final):
        horas.append(str(db.loc[element, 'Hora']))
        glucosa.append(int(db.loc[element, 'mg/dL']))
        condicion.append(str(db.loc[element, 'Condición']))

    if len(horas) <= 10:
        puntosx = makeX(horas)
        return puntosx, horas, glucosa, condicion
    else: 
        while (len(rand_horas)<10):
            rand_num = random.randint(0, (len(horas)-1))
            element_h = horas[rand_num]
            element_g = glucosa[rand_num]
            element_c = condicion[rand_num]
            if element_h not in rand_horas:
                rand_horas.append(element_h)
                rand_glucosa.append(element_g)
                rand_condicion.append(element_c)
        puntosx = makeX(rand_horas)
        return puntosx, rand_horas, rand_glucosa, rand_condicion

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

def Trapecio(x,y):
    l=len(x)
    h=x[2]-x[1]
    I=(0.5*(y[1]+y[2]))*h
    i=1
    for i in range(l-1):
        h=x[i+1] - x[i]
        I+=(0.5*y[i]+y[i+1])*h
    return I
