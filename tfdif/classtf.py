import sys
import glob
import numpy
from matplotlib import pyplot
def dist(v1,v2): 
	return numpy.linalg.norm(v1-v2)
# Structures holding documents and terms
document_list = []
document_ids = {} 
token_list = [] 
token_ids = {} 
tokens =[]
for filename in glob.glob('pages2/*'):
	# Read the document as list of blank-separated tokens
	f = open (filename, 'r')
	#tokens1 = f.read().split()
	for line in f:
		values = line.split()
		for v in values:
			
				tokens.append(v)

	f.close()
	# Get the document name as last part of path
	article_name = filename[filename.rfind('/')+1:]
	sys.stderr.write ('Processing document %s...\n' % article_name)
	# Document's ID is the length of the current document list
	doc_id = len(document_list)
	# Insert ID in inverse list
	document_ids[article_name] = doc_id
	# Populate token structure for all tokens in document
	for t in tokens:
		# Only if token hasn't been seen yet
		if t not in token_ids:
			# Token's ID is token list length
			token_ids[t] = len(token_list) # establece los ides para cada palabra
			# Append token to list
			token_list.append(t) # mantiene el listado d elas palabras
	# Transform the document's token list into the corresponding ID list
	tids = [token_ids[t] for t in tokens]
	# Store the document as both its token ID list and the corresponding set
	# Also remember the document's name
	document_list.append({
		'name': article_name,
		'tokens': tids,
		'set': set(tids)
	})

# At the end of the loop, we have the total number of documents and tokens
number_of_documents = len(document_list)
number_of_tokens = len(token_list)
sys.stderr.write ('%d documents, %d tokens\n' % (number_of_documents, number_of_tokens))

##############################################
#
# Building the TF-IDF matrix

sys.stderr.write ('Building the TF matrix and counting term occurrencies\n')
# For each term, count how many documents contain it (to compute IDF)
token_count = [0] * number_of_tokens
# Alloc the |T|x|D| TFIDF matrix. No need to initialize its entries
TFIDF = numpy.empty((number_of_tokens,number_of_documents), dtype=float)
# Scan the document list
for i,doc in enumerate(document_list):
	# For each term, count the number of occurrences within the document
	# Initialize with zeros
	n_dt = [0] * number_of_tokens
	# For all token IDs in document
	for tid in doc['tokens']:
		# if first occurrence, increase global count for IDF
		if n_dt[tid] == 0:
			token_count[tid] += 1
		# increase local count
		n_dt[tid] += 1
	# Normalize local count by document length obtaining TF vector;
	# store it as the i-th column of the TFIDF matrix.
	TFIDF[:,i] = numpy.array(n_dt, dtype=float) / len(doc['tokens'])

# Transform the global count into IDF
sys.stderr.write ('Computing the IDF vector\n')
IDF = numpy.log10(number_of_documents / numpy.array(+2, dtype=float))

# Apply IDF multipliers to the rows of the TF matrix (left-multiply by diagonal IDF values)
sys.stderr.write ('Multiplying IDF coefficients into the TF matrix...\n')
# First method: explicitly multiply each row by the appropriate IDF coefficient
for row in TFIDF:
	row *= IDF

query = "Business management profit administration"
vector = [0] * number_of_tokens;
for token in query.split():
	if token_ids[token] is not None:
		position = token_ids[token]
		vector[position] = vector[position] + 1
vectorTFIDF = vector * IDF
distancias = []
for f in TFIDF.T:
	distancias.append(dist(vectorTFIDF,f))
b = numpy.argsort(distancias)
print b[0:10]

for a in b[0:10]:
	print document_list[a]['name']

