#!/usr/bin/python

from aocd import get_data

d = get_data(day=6).split('\n')
#d = ['1, 1',
#     '1, 6',
#     '8, 3',
#     '3, 4',
#     '5, 5',
#     '8, 9']
points = []


# [minx = 1024, maxx = 0, miny = 1024, maxy = 0]
minx = 100000
maxx = 0
miny = 100000
maxy= 0

excluded = []

for line in d:
    coordx = int(line.split(', ')[0])
    coordy = int(line.split(', ')[1])
    points.append([coordx, coordy])

    if coordx < minx:
        minx = coordx
    elif coordx > maxx:
        maxx = coordx
    if coordy <= miny:
        miny = coordy
    elif coordy >= maxy:
        maxy = coordy


for i in range(len(points)):
    if points[i][0] == minx or points[i][0] == maxx or points[i][1] == miny or points[i][1] == maxy:
        excluded.append(i)

#print(excluded)

matrix = [['x' for x in range(maxx + 1)] for y in range(maxy + 1)]
for y in range(maxy + 1):
    for x in range(maxx + 1 ):
        distmin = 100000
        tie = False
        for point in points:
            if abs(point[1] - y) + abs(point[0] - x) == distmin:
                tie = True
            if abs(point[1] - y) + abs(point[0] - x) < distmin:
                distmin = abs(point[1] -y) + abs(point[0] - x)
                closest = points.index(point)
                tie = False
        if tie:
            matrix[y][x] = '.'
        else:
            matrix[y][x] = closest

#print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in matrix]))

maxsurface = 0
for i in range(len(points)):
    surface = 0
    if i not in excluded:
        for y in range(maxy + 1):
            surface += matrix[y].count(i)
        if surface > maxsurface:
            maxsurface = surface

print(maxsurface)
