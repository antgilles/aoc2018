#!/usr/bin/python

#from aocd import get_data
with open('day12-input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
d = [x.strip() for x in content]

#d = get_data().split('\n')

initial = d.pop(0).split(' ')[2]
d.pop(0)

matching = []
for i in d:
    matching.append([list(i.split(' ')[0]), i.split(' ')[2]])


initial = addendum + list(initial) + addendum
print(initial)
print(matching)

for gen in range(20):
    next = ['.'] * len(initial)
    for i in range(2, len(initial) -1):
        for match,plant in matching:
            if initial[i - 2 : i + 3] == match:

                next[i] = plant
    initial = list(next)
    print(''.join(next))

result = 0
for i in range(len(initial)):
    if initial[i] == '#':
        result += i - 50
print(result)