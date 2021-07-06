import pandas as pd
from datetime import date, datetime
import time
import random

def makeX(horas, time):
    tiempo = []
    (h, m) = time.split(':')
    zero = int(h) + (int(m)/60)
    for hour in horas:
        (h, m, s) = hour.split(':')
        decimaltime = int(h) + (int(m)/60)
        result = decimaltime - zero
        tiempo.append(result)
    return tiempo

def getPoints(db, hora_med, di, df):
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
        puntosx = makeX(horas, hora_med)
        return puntosx, horas, glucosa, condicion
    else: 
        while (len(rand_horas)<10):
            rand_num = random.randint(0, (len(horas)-1))
            element_h = horas[rand_num]
            element_g = glucosa[rand_num]
            element_c = condicion[rand_num]
            if element not in rand_horas:
                rand_horas.append(element_h)
                rand_glucosa.append(element_g)
                rand_condicion.append(element_c)
        puntosx = makeX(rand_horas, hora_med)
        return puntosx, rand_horas, rand_glucosa, rand_condicion

def RazonCambio(x, y):
    n = len(x)
    dx = []
    dx[0] = (y[1] - y[0])/(x[1] - x[0])
    i = 2
    while i != (n-1):
        dx[i] = (y[i+1] - y[i-1])/(x[i+1] - x[i-1])
        i = i + 1
    dx[n] =  (y[n] - y[n-1])/(x[n] - x[n-1])
    return dx
