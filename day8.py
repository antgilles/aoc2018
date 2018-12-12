#!/usr/bin/python

from aocd import get_data

d = get_data(day = 8).split(' ')
#d = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' ')


def getheader(data):
    numchild = int(data.pop(0))
    nummeta = int(data.pop(0))
    result = 0
    while numchild:
        result += getheader(data)
        numchild = numchild - 1
    for i in range(nummeta):
        result += int(data.pop(0))
    return(result)

result = getheader(d)

print(result)