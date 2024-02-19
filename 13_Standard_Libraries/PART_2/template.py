from string import Template
t = Template('Return the $item to $owner.')
d = dict(item = 'Unladen swallow')
#print(t.substitute(d))
print(t.safe_substitute(d))