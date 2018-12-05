#!/usr/bin/python

from aocd import get_data
import operator

data = get_data()
#data = 'dabAcCaCBAcCcaDA'
alphabet={}

for x in [chr(x) for x in range(ord('a'), ord('z')+1)]:
    d = str(data).translate(None, x + x.upper())
    i = 0
    while i + 1 < len(d):
        if (d[i].lower() == d[i+1].lower() and ((d[i].isupper()  and  d[i+1].islower()) or (d[i].islower()  and  d[i+1].isupper()))):
            d = d[:i] + d[i+2:]
            if i != 0:
                i -= 1
        else:
            i += 1
    alphabet[x] = len(d)
print(min(alphabet.iteritems(), key=operator.itemgetter(1)))[1]