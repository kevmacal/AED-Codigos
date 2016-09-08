import pandas as pd
import gc
import math
from pandas import Series,DataFrame
data = pd.read_csv("current.csv") #dataset original
del data['latitud'] 
del data['longitud']
del data['tipo'] 
del data['lugar']
del data['direccion']
del data['fecha'] 
termslist = {}
#print data.shape[0]
#data = data.head(1000)
#print next(data.iterrows())[1]
for i, row in data.iterrows():
	linea = row['descripcion']
	tokens = linea.split()
	for word in tokens:
		if word in termslist:
			termslist[word] = termslist[word] + 1
		else:
			termslist[word] = 1
print "LISTA DE TERMINOS LISTA"
tf = DataFrame(index = range(0,data.shape[0]),columns = termslist.keys())
tf[:].fillna(0, inplace=True)
print "INICIALIZO TF"
fila = 0
for i, row in data.iterrows():
	linea = row['descripcion']
	tokens = linea.split()
	for word in tokens:
		if pd.isnull(tf.ix[fila,word]) == True:
			tf.ix[fila,word] = 1
		else:
			tf.ix[fila,word] = tf.ix[fila,word] + 1
	tf.ix[fila] = tf.ix[fila] / len(tokens)
	fila = fila + 1
	print "Fila: ", fila
#print tf
print "TF MATRIX LISTO"
idf = Series()
#print idf.index
for term in termslist.keys():
	apariciones = termslist[term]
	totaldoc = data.shape[0]
	argumento = totaldoc / (1 + apariciones)
	#print argumento
	test = Series({term : math.log(argumento)})
	idf = idf.add(test, fill_value=0)
#print idf
print "IDF LISTO"
gc.collect()
for i, row in tf.iterrows():
	print i
	tf.ix[i] = row.multiply(idf)
	#gc.collect()

#print tf
#print idf 
#tfidf = tf.apply(lambda x: x.multiply(idf), axis = 1)
#print tfidf
tf.to_csv('tfidf.csv')
idf.to_csv('idf.csv')