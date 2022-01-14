import numpy as np
import matplotlib.pyplot as plt

coords = graph = []
avoid = 0

with open('Day_5_Input.txt', "r") as f:
    coords = (f.read().splitlines())

for i in (range(len(coords))):
    coords[i] = coords[i].split()

for i in range(len(coords)):
    k = 0
    while k in range(len(coords[i])):
        if coords[i][k] == '->':
            coords[i].pop(k)
        else:
            k += 1

for i in range(len(coords)):
    for k in range(len(coords[i])):
        coords[i][k] = coords[i][k].split(',')

for i in range(len(coords)):
    for k in range(len(coords[i])):
        for j in range(len(coords[i][k])):
            coords[i][k][j] = int(coords[i][k][j])

rows = 1000
cols = 1000
graph = [[0 for x in range(rows)] for y in range(cols)]


for i in range(len(coords)):
    start = coords[i][0]
    end = coords[i][1]
    movement = (np.subtract(end,start))

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]
    xpoints = np.array([x1,x2])
    ypoints = np.array([y1,y2])
    plt.plot(xpoints, ypoints)
    y = 0
    x = 0
    if (movement[0]) >= 0:
        if movement[1] == 0:
            while x <= (movement[0]):
                graph[(x1+x)][y1] = graph[(x1+x)][y1] + 1
                x += 1
    else:
        if movement[1] == 0:
            while x >= (movement[0]):
                graph[x1+x][y1] = graph[x1+x][y1] + 1
                x -= 1
    if (movement[1]) >= 0:
        if movement[0] == 0:
            while y <= (movement[1]):
                graph[x1][y1+y] = graph[x1][y1+y] + 1
                y += 1
    else:
        if movement[0] == 0:
            while y >= (movement[1]):
                graph[x1][y1+y] = graph[x1][y1+y] + 1
                y -= 1

    if (movement[0] != 0) and (movement[1] != 0):
        if x1 > x2:
            x = -1
        else:
            x = 1
        if y1 > y2:
            y = -1
        else:
            y = 1
        if movement[0] > 0:
            m = movement[0] + 1
        else:
            m = -(movement[0]) + 1

        for k in range(m):
            xstep = (k*x)
            ystep = (k*y)
            graph[x1+xstep][y1+ystep] = graph[x1+xstep][y1+ystep] + 1


for i in range(len(graph)):
    for k in range(len(graph)):
        if graph[i][k] >= 2:
            avoid += 1

plt.show()
print(avoid)


