import pandas as pd
import datetime
from pandas import Series,DataFrame
puredata = pd.read_csv("data.csv") #dataset original
df = DataFrame()
puredata['date'] = pd.to_datetime(puredata['Date'])

crimes = puredata[ puredata['date'] >= datetime.date(year=2015,month=1,day=1)]
df['lat'] = crimes['Latitude']
df['lon'] = crimes['Longitude']
df.reset_index().to_json('geodata.json',orient='values')