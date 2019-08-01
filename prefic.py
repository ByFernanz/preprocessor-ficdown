import fileinput

stage = 0
properties = {}
for line in fileinput.input():
    if line.startswith('---'):
    	stage += 1
    elif stage == 1:
    	[prop, val] = line.split(': ')
    	properties[prop] = val.splitlines()[0]
    elif stage == 2:
    	for prop in properties:
    		line = line.replace(''.join(['__', prop, '__']), properties[prop])
    	print(line, end='')