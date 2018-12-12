#!/usr/bin/python

from aocd import get_data

d = get_data(day = 8).split(' ')
#d = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' ')


def getheader(data):
    numchild = int(data.pop(0))
    nummeta = int(data.pop(0))
    result = 0
    childres = []
    if numchild == 0:
        for i in range(nummeta):
            result += int(data.pop(0))
    else:
        while numchild:
            childres.append(getheader(data))
            numchild = numchild - 1
        for i in range(nummeta):
            metaval = int(data.pop(0))
            if metaval < len(childres) + 1:
                result += int(childres[metaval - 1])
    return(result)

result = getheader(d)

print(result)