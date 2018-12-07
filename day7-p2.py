#!/usr/bin/python

from aocd import get_data
import re

NBLETTER = 26
nbworker = 5
DELAYPERTASK = 60

alphabet = [[] for i in range(NBLETTER)]
d = get_data().split('\n')

result = ""

for line in d:
    m = re.match(r'Step (\S+) must be finished before step (\S+) can begin.', line)
    alphabet[ord(m.group(2)) - 65].append(m.group(1))


letterrest = NBLETTER
timer = 0
alphabettimer = [-1] * NBLETTER

while letterrest > 0:

    for k in range(len(alphabet)):
        if len(alphabet[k]) == 0 and nbworker > 0 and alphabettimer[k] == -1:
            result += chr(k + 65)
            nbworker -= 1
            alphabettimer[k] = DELAYPERTASK + k + 1

    for i in range(len(alphabettimer)):
        if alphabettimer[i] > 0:
            alphabettimer[i]  -= 1
        if alphabettimer[i] == 0:
            nbworker += 1
            letterrest -= 1
            alphabettimer[i] = -2
            for j in range(len(alphabet)):
                if chr(i + 65) in alphabet[j]:
                    alphabet[j].remove(chr(i + 65))
    timer += 1

print(timer)
