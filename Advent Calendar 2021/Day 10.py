

with open('Day_10_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

symbols = {'<': 1, '{': 2, '[': 3, '(': 4, ')': -4, ']': -3, '}': -2, '>': -1}
points = {-1: 25137, -2: 1197, -3: 57, -4: 3}
illegal = []

for i in range(len(myinput)):
    symbollist = []
    for k in range(len(myinput[i])):
        if myinput[i][k] in symbols:
            if symbols[myinput[i][k]] > 0:
               symbollist.append(symbols[myinput[i][k]])
            elif symbollist[-1] == (symbols[myinput[i][k]])*-1:
                symbollist.pop()
            else:
                print('expected ' + str(symbollist[-1]) + ' but found ' + str(symbols[myinput[i][k]]))
                illegal.append(symbols[myinput[i][k]])
                break
total = 0
for i in range(4):
    total = total + points[-(i+1)] * illegal.count(-(i+1))

print(symbols)
print(illegal)
print(total)