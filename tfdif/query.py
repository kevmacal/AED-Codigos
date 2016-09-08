import pandas as pd
import gc
import math
from pandas import Series,DataFrame
from scipy.spatial.distance import cosine
idf = Series.from_csv("idf.csv")
tfidf = pd.read_csv("tfidf.csv",index_col = 0)
#print tfidf.head(5)
#print idf.size
tfquery = Series()

linea = "THEFT IS A SIMPLE TASK FOR CRIME BUT VIOLATION IS NOT" # QUERY A EVALUAR
tokens = linea.split()	
for word in tokens:
	if word in tfidf.columns:
		if word in tfquery:
			tfquery[word] = tfquery[word] + 1
		else :
			test = Series({word : 1})
			tfquery = tfquery.add(test, fill_value=0)
tfquery = tfquery/len(tokens)
tfquery = tfquery.multiply(idf,fill_value = 0)
#print tfquery
#print(1 - cosine(df["col1"], df["col2"]))
distancias = Series()
for i, row in tfidf.iterrows():
	test = Series({i : 1 - cosine(row, tfquery)})
	distancias = distancias.add(test, fill_value=0)
#tfidf.sort_values('DISTANCIAQUERY',ascending=False)
#print tfidf.head(10)['DISTANCIAQUERY']
distancias.sort_values(ascending = False,inplace = True)
print distancias[0:10]