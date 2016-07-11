import pandas as pd
import datetime
from pandas import Series,DataFrame

airbnbRooms = pd.read_csv("final_resultadoScrap.csv")#dataser del airbnb
df = DataFrame()
df['lat'] = airbnbRooms['latitud']
df['lon'] = airbnbRooms['longitud']
df.reset_index().to_json('geodatairbnb.json',orient='values')