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

map = [[0]*(max(x))]*max(y)


