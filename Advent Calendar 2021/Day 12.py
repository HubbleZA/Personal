with open('Day_12_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

caves = {}
for i in myinput:
    [a, b] = i.split('-')
    if a not in caves:
        caves[a] = []
    if b not in caves:
        caves[b] = []
    caves[a].append(b)
    caves[b].append(a)

print(caves)