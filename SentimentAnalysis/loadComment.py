import pickle

import re

file = 'items.jl'


pattern = re.compile(r'.*?("name":.*?),.*?')
pattern2 = re.compile(r'.*?("id":.*?),.*?')
pattern3 = re.compile(r'.*?("assignments_feedback_comment":.*?), "shortName.*?')

dicts_from_file = []
with open(file,'r') as inf:
    for l in inf:
    	line = re.findall(pattern,l)
    	line2 = re.findall(pattern2,l)
    	line3 = re.findall(pattern3,l)
    	# line = line + line2
    	# print line
    	# print line2
    	try:
    		line = '{' + ('').join(line) + ',' + ('').join(line2) + ',' + ('').join(line3) + '}'
    		dicts_from_file.append(eval(line))
    	except:
    		print 'E'

# for d in dicts_from_file:
	# if d['assignments_feedback_comment'] is not 0:
	# print('Id: %s, Name: %s, Comments: %s' % (d['id'],d['name'],d['assignments_feedback_comment']))
	
pickle.dump(dicts_from_file, open("assignments_feedback_comment.p", "wb")) 
