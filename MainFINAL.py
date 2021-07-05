import pandas as pd
import os
import datetime

db = pd.read_excel('Glucosa-Project.xlsx')
for index, row in db.iterrows():
    if db.isnull(db.loc[index]) == True:
        db = db.drop(row['Fecha'].index)

dates = db['Fecha']
gluc = db['mg/dL']
times = db['Hora']
condition = db['Condición']
"""
for index, row in db.iterrows():
    print(row['Fecha'])
    """


