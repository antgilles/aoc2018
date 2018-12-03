#!/usr/bin/python

from aocd import get_data
import re


d = get_data().split('\n')
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
matrix = [['.' for i in range(2048)] for j in range(2048)]
result = 0
#d = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
for line in d:
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    id = m.group(1)
    coordx = int(m.group(2))
    coordy = int(m.group(3))
    width = int(m.group(4))
    height = int(m.group(5))

    for i in range(coordx, coordx + width):
        for j in range(coordy, coordy + height):
            if matrix[i][j] == '.':
                matrix[i][j] = id
            elif matrix[i][j] != '.' and matrix[i][j] != 'x':
                result += 1
                matrix[i][j] = 'x'


print(result)
