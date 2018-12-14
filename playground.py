from collections import OrderedDict
tdict = OrderedDict()
tdict['a'] = 5
tdict['b'] = 6
print(tdict)
tdict.move_to_end('a')
print(tdict)