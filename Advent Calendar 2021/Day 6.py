from collections import Counter

fishnum = fishdays = fish = temp = []
new = days = 0
x = {}

with open('Day_6_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

myinput[0] = myinput[0].split(",")

for i in range(len(myinput)):
    for k in myinput[i]:
        fishnum.append(int(k))

fishnum.sort()

x = Counter(fishnum)
x = dict(x)
fishnum = list(dict.fromkeys(fishnum))
fishdays = list(dict.fromkeys(fishnum))

for i in range(len(fishnum)):
    fishnum[i] = x[fishnum[i]]

fish = list(zip(fishdays, fishnum))

for i in range(len(fish)):
    fish[i] = list(fish[i])

userinput = int(input("Please enter the amount of days: "))

while days < userinput:
    for i in range(len(fish)):
        fish[i][0] = fish[i][0] - 1
        if fish[i][0] == -1:
            fish[i][0] = 6
            new = 1*fish[i][1]
            fish.append([8, new])
    result = {}
    for k, v in fish:
        result[k] = result.get(k, 0) + v
    fish.clear()
    for k ,v in result.items():
        temp = [k,v]
        fish.append(temp)
    days += 1
    new = 0
print(fish)
m = 0
for i in range(len(fish)):
    m = m + (fish[i][1])

print(m)


