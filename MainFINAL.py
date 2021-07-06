import pandas as pd
import os
import datetime

db = pd.read_excel('Glucosa-Project.xlsx')
database = db.dropna()

dates = database['Fecha']
gluc = database['mg/dL']
times = database['Hora']
condition = database['Condición']

for index, row in db2.iterrows():
    print(row['Fecha'])


