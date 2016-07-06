import pandas as pd
form pandas import DataFrame, Series
import numpy as np

data = pandas.load_csv('Crimes_-_2001_to_present.csv')
print data.head(1)
print "\n"
#Filtro de datos para escoger solo el año 2016
data_filtrado = data[data.Year==2016]
print data_filtrado.head(2)
print "\n"
#Resumen de los datos numericos
print data_filtrado.describe()
