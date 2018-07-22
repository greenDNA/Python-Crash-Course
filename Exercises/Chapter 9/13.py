from collections import OrderedDict

terms = OrderedDict()
terms['dictionary'] = 'function in python that maps a key to a value'
for item, defi in terms.items():
    print("{}: {}".format(item, defi))
