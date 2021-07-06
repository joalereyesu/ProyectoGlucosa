import pandas as pd
from datetime import date, datetime
import time

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

def checkDates(db, di, df):
    #datei = datetime.strptime(di, '%Y-%m-%d')
    #datef = datetime.strptime(df, '%Y-%m-%d')
    print(db.date_range(start = di, end = df))