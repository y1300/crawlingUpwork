import pickle
from textblob import TextBlob
import re

'''
Set tartget to 'description' or 'assignments_feedback_comment' to rank by descriptions or comments repectively
'''
target = 'description'
# target = 'assignments_feedback_comment'

dicts_from_file = pickle.load(open(target+".p", "rb"))

idWithDesc = []

for d in dicts_from_file:
	# print d['assignments_feedback_comment'] == '{}'
	# if d['assignments_feedback_comment'] != '{}':
	# 	print('Id: %s, Name: %s, Comments: %s' % (d['id'],d['name'],d['assignments_feedback_comment']))

	try:
		if d[target] != '{}':
			idWithDesc.append(d)
	except:
		print 'no ' + target

# print len(idWithDesc)

def clean_line(line):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())



senti = []
for line in idWithDesc:
	senti.append(TextBlob(clean_line(line[target])))
	# print line['description']

for i in range(len(idWithDesc)):
	idWithDesc[i]['sentiment'] = senti[i].sentiment.polarity

idWithDesc = sorted(idWithDesc, key = lambda x:x['sentiment'], reverse = True)

# senti = []

f = open('rankedBySentiments.txt', "wb")
 
for row in idWithDesc:
	f.write(str("{0:.4f}".format(row['sentiment'])) +', '+row['id'][1:]+', '+ row['name'] + ', '+ row[target] + '\n')
	# senti.append(row['sentiment'])

f.close()

# open('senti.txt','w').write(str(senti))
