#!/usr/bin/python

from aocd import get_data
import re

NBLETTER = 26

alphabet = [[] for i in range(NBLETTER)]
d = get_data().split('\n')


result = ""

for line in d:
    m = re.match(r'Step (\S+) must be finished before step (\S+) can begin.', line)
    alphabet[ord(m.group(2)) - 65].append(m.group(1))

for i in range(len(alphabet)):
    for letter in alphabet:
        if len(letter) == 0:
            result += chr(alphabet.index(letter) + 65)
            letter.append(i)
            for j in range(len(alphabet)):
                if chr(alphabet.index(letter) + 65) in alphabet[j]:
                    alphabet[j].remove(chr(alphabet.index(letter) + 65))
            break

print(result)
