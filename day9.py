#!/usr/bin/python

from aocd import get_data
import itertools

NBPLAYER = 430
NBMARBLE = 7158800

result = [0] * NBPLAYER

circle = [0]

current = 0
value = 1
while True:
    if value != 0 and value % 23 == 0:
        result[(value - 1) % NBPLAYER] += value
        result[(value - 1) % NBPLAYER] += circle[current - 7]
        circle.pop(current - 7)
        current = current - 7 % (len(circle) -1)

    elif len(circle) < 2:
        current = len(circle)
        circle.append(value)

    else:
        current = (current + 2) % (len(circle))
        circle.insert(current,value)
    value += 1

    if value > NBMARBLE:
        break
    if value % 10000 == 0:
        print(value)
print(max(result))