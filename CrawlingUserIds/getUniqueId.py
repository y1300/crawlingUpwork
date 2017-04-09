output = open('Output.txt','r').read()
set = list(set(output.split('\n')))
print len(set)
ids = []
for e in set:
	if len(e) == 19: # To filter those damaged user Ids
		ids.append(e)
open('ids.txt','w').write(('\n').join(ids))
