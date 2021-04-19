# 4.18 Sunday
# Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key': 'hello'}
print d['simple_key']

# Grab 'hello'
e = {'k1': {'k2': 'hello'}}
print e['k1']['k2']

# Grab 'hello'
# Getting a little trickier
f = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print f['k1'][0]['nest_key'][1][0]

# Grab hello
# This will be hard and annoying!
g = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print g['k1'][2]['k2'][1]['tough'][2][0]

# Can you sort a dictionary? Why or why not?
# No, Because normal dictionaries are mappings not a sequence.
