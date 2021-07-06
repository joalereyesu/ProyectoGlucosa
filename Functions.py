import pandas as pd
from datetime import date, datetime
import time
import random

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
