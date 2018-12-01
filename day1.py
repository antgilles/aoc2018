#!/usr/bin/python

from aocd import get_data

d = get_data().split('\n')
result = 0
for i in d:
    result += int(i)
print(result)
