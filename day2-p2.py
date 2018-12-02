#!/usr/bin/python

from aocd import get_data

d = get_data().split('\n')

#d=['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

for currentline in d:
    diff = 0
    for compareline in d:
        diff = 0
        i = 0
        for c in currentline:
            if c != compareline[i]:
                diff += 1
                delcharpos=i
                if diff > 1:
                    break
            i += 1
        if diff == 1:
            result1 = currentline
            result2 = compareline
            result =  currentline[:delcharpos] + currentline[delcharpos+1:]
            break

print(result)
