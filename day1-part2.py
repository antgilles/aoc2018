#!/usr/bin/python

from aocd import get_data
import itertools

d = get_data().split('\n')
freq = 0
met = [0]
for i in itertools.cycle(d):
    freq += int(i)
    if freq in met:
        result = freq
        break
    met.append(freq)

print(result)
