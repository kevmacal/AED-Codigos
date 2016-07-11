import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Crimes_-_2001_to_present.csv')
data_airbnb = pd.read_csv('final_resultadoScrap.csv')

print (data.head(1))

data_filtrado = data[data.Year==2016]
data_filtrado2 = data[data.Year==2015]
datos_filtrados = [data_filtrado,data_filtrado2]
resultado = pd.concat(datos_filtrados)

resultado.to_csv('dataset2015-2016.csv')

temp = resultado['Primary Type'].value_counts()
print temp


probability = (temp/temp.sum()) 

print (probability)

description = probability.describe()

print description

temp = resultado[['ID','Primary Type','Date','Latitude','Longitude']].groupby('Primary Type')

print temp

filtro = data_airbnb['cost'].describe()
print (filtro)

#locations=[-87.939195, 41.656424, -87.531348, 42.019607])  # Chicago
