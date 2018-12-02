#!/usr/bin/python

from aocd import get_data

d = get_data().split('\n')

two = 0
three = 0
for line in d:
    alphabet = [0] * 26
    for letter in line:
        alphabet[ord(letter) - 97] += 1
    if 2 in alphabet:
        two += 1
    if 3 in alphabet:
        three += 1

result = two * three
print(result)
