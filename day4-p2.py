#!/usr/bin/python

from aocd import get_data
import re

d = get_data().split('\n')

d.sort()
reg={}

for line in d:
    m = re.match(r'\[\d+\-\d+\-\d+ \d+:(\d+)\] (\w+) (\S+)', line)
    if m.group(2) == 'Guard':
        cur = int(m.group(3)[1:])
        if cur not in reg:
            reg[cur] = [0] * 60
    elif m.group(2) == 'falls':
        begin = int(m.group(1))
    elif m.group(2) == 'wakes':
        end = int(m.group(1))
        for i in range(begin, end):
            reg[cur][i] += 1

recordguard = 0
record = 0

for guard, shift in reg.iteritems():
    curmax = max(reg[guard])
    if curmax > record:
        record = curmax
        recordguard = guard
minute = reg[recordguard].index(record)

result = recordguard * minute
print(result)