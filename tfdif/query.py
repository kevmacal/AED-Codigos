import pandas as pd
from scipy import spatial
import gc
import math
from pandas import Series,DataFrame
from scipy.spatial.distance import cosine
import numpy
def dist(v1,v2): 
	return numpy.linalg.norm(v1-v2)
idf = Series.from_csv("idf.csv")
tfidf = pd.read_csv("tfidf.csv",index_col = 0)
#print tfidf.head(5)
#print idf.size
tfquery = Series()

linea = "Armed Robbery Suspect Arrested w/ Handgun" # QUERY A EVALUAR
linea = linea.upper()
tokens = linea.split()	
for word in tokens:
	if word in tfidf.columns:
		print word
		if word in tfquery:
			tfquery[word] = tfquery[word] + 1
		else :
			tfidf[word] = 0
			test = Series({word : 1})
			tfquery = tfquery.add(test, fill_value=0)
tfquery = tfquery/len(tokens)
tfquery = tfquery.multiply(idf,fill_value = 0)
print "TERMINO TFIDF"

vectorTFIDF = tfquery.as_matrix()
distancias = []
for i , f in tfidf.iterrows():
	#distancias.append(dist(vectorTFIDF,f.as_matrix()))
	distancias.append(1 - spatial.distance.cosine(f.as_matrix(), vectorTFIDF))
#b = numpy.argsort(distancias)
distancias = sorted(distancias,reverse=True)
print distancias[0:100]



#tfquery.to_csv('query.csv')
# cache = []
# distancias = Series()
# for i, row in tfidf.iterrows():
# 	d = cosine(row, tfquery)
# 	test = Series({i : d})
# 	if d > 0.75:
# 		print row
# 		print tfquery
# 		cache.append(d)
# 	distancias = distancias.add(test, fill_value=0)
# print "DISTANCIAS TERMINADAS"

# if len(cache) > 0:
# 	print "VALORES CACHEADOS"
# 	sorted(cache)
# 	print cache
# else:
# 	distancias.sort_values(ascending = False,inplace = True)
# 	print distancias[0:10]