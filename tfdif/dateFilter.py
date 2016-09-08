import pandas as pd
import datetime
from pandas import Series,DataFrame
puredata = pd.read_csv("datapura.csv") #dataset original

df = DataFrame()
puredata['date'] = pd.to_datetime(puredata['Date'])
#print puredata.head()
crimes = puredata[ puredata['date'] >= datetime.date(year=2016,month=1,day=1)]
df['latitud'] = crimes['Latitude']
df['longitud'] = crimes['Longitude']
df['tipo'] = crimes['Primary Type']
df['descripcion'] = crimes['Description']
df['lugar'] = crimes['Location Description']
df['direccion'] = crimes['Block']
df['fecha'] = crimes['date']
df.to_csv('current.csv')
