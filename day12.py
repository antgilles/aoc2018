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

addendum = ['.'] * 4
decalage = 0
gen = 0

print(initial)
print(matching)

while gen < 20:
    initial = addendum + list(initial) + addendum
    next = ['.'] * len(initial)
    for i in range(2, len(initial) -1):
        for match,plant in matching:
            if initial[i - 2 : i + 3] == match:

                next[i] = plant
    initial = list(next)
    decalage += 4
    while initial[0] == '.':
        initial.pop(0)
        decalage -= 1
    while initial[-1] == '.':
        initial.pop()
    #print(''.join(initial))
    gen+=1
    if gen % 10000 == 0:
        print(gen)
result = 0
for i in range(len(initial)):
    if initial[i] == '#':
        result += i - decalage
print(result)