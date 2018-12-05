#!/usr/bin/python

from aocd import get_data

d = get_data()
#d = 'dabAcCaCBAcCcaDA'

i = 0
while i + 1 < len(d):
    if (d[i].lower() == d[i+1].lower() and ((d[i].isupper()  and  d[i+1].islower()) or (d[i].islower()  and  d[i+1].isupper()))):
        tmp = d[:i] + d[i+2:]
        d = tmp
        i -= 1
    else:
        i += 1

print(len(d))