with open('Day_13_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

instructions = []
points = []

for i in range(len(myinput)):
    if myinput[i] == '':
        points = ((myinput[0:i]).copy())
        instructions = ((myinput[(i+1):len(myinput)]).copy())

print(points)
print(instructions)

x = []
y = []

for i in points:
    a,b = i.split(',')
    x.append(int(a))
    y.append(int(b))


map = [[0for i in range((max(x))+1)] for j in range((max(y))+1)]

for i in range(len(x)):
    (map[(y[i])][(x[i])]) = 1



def fold(axis, line, map):
    fmap = []
    if axis == 'x':
        for i in range(len(map)):
            fmap = (map[i][line:])
            map[i] = (map[i][0:line])
            print(len(fmap))
            a = (fmap[i][::-1])
            b = map[i]
            for k in range(len(a)):
                if a[k-1] + b[k-1] > 0:
                    map[i][k-1] = 1

    elif axis == 'y':
        fmap = map[line:]
        map = (map[0:line])
        print(len(map))
        print(len(fmap))
        while len(fmap) > len(map):
            fmap = fmap[0:len(fmap)-1]

        for i in range(len(fmap)):
            a = (fmap[(len(fmap)-1)-i])
            b = map[i]
            for k in range(len(a)):
                if a[k-1] + b[k-1] > 0:
                    map[i][k-1] = 1

    else:
        print('Not readying axis')

    return map

axis = ''
line = 0
folds = 0
for i in range(len(instructions)):
    for k in range(len(instructions[i])):
        if instructions[i][k] == '=':
            axis = (instructions[i][k-1])
            line = int(instructions[i][(k+1):])-1
            print(instructions[i])
            map = fold(axis, line, map)
            dots = 0
            folds += 1
            for j in range(len(map)):
                for l in range(len(map[j])):
                    if map[j][l] == 0:
                        dots += 1
            print('There are ' + str(dots) + ' dots after ' + str(folds) + ' folds.')





# 584071 too high
# 583178 too high
