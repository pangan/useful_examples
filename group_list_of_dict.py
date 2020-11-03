import itertools

my_list = [{'topic': 't2', 'value': 4, 'other': 'text1'},
           {'topic': 't1', 'value': 2, 'other': 'text2'},
           {'topic': 't2', 'value': 3, 'other': 'text3'},
           {'topic': 't1', 'value': 5, 'other': 'del'}]

newlist = list(filter(lambda x: x['other'] != 'del', my_list))

uniquekeys = []
newlist = sorted(newlist, key=lambda k: (k['topic'], k['value']))
keyfunc = lambda x: x['topic']
for kk, g in itertools.groupby(newlist, keyfunc):
    a = list(g)
    max_val = max(a, key=lambda k: k['value'])
    uniquekeys.append(max_val)

print (uniquekeys)
