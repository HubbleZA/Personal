from collections import Counter

with open('Day_9_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

nums = []
cords = []
for i in range(len(myinput)):
    for k in range(len(myinput[i])):
        num = myinput[i][k]
        if i == 0 and 0 < k < ((myinput[i]).__len__() - 1):
            if num < myinput[i][k + 1] and num < myinput[i][k - 1] and num < myinput[i + 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif i == len(myinput) - 1 and 0 < k < ((myinput[i]).__len__() - 1):
            if num < myinput[i][k + 1] and num < myinput[i][k - 1] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif k == 0 and 0 < i < len(myinput):
            if num < myinput[i][k + 1] and num < myinput[i + 1][k] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif k == len(myinput[i]) - 1 and 0 < i < len(myinput):
            if num < myinput[i][k - 1] and num < myinput[i + 1][k] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif i == 0 and k == 0:
            pass
        elif i == 0 and k == ((myinput[i]).__len__()) - 1:
            pass
        elif k == 0 and i == len(myinput):
            pass
        elif k == ((myinput[i]).__len__() - 1) and i == len(myinput):
            pass
        else:
            if num < myinput[i][k + 1] and num < myinput[i][k - 1] and num < myinput[i + 1][k] and num < myinput[i - 1][
                k]:
                nums.append(num)
                cords.append((i, k))
sum = 0
for i in nums:
    sum += (int(i) + 1)
test1 = []
for k in range(len(myinput)):
    test1.append([myinput[k][i] for i in range(len(myinput[k]))])


def check(input, x, y, numcords):
    if x < 0 or y < 0 or x >= len(input) - 1 or y >= ((input[y]).__len__()) - 1 or input[y][x] == '9' or (
    y, x) in numcords:
        return
    numcords.append((y, x))
    check(input, x, y + 1, numcords)
    check(input, x, y - 1, numcords)
    check(input, x + 1, y, numcords)
    check(input, x - 1, y, numcords)


numkept = []
for i in cords:
    y = i[0]
    x = i[1]
    numcords = []
    check(myinput, x, y, numcords)
    numkept.append(len(numcords))

numkept = sorted(numkept, reverse=True)
n = 0
total = 1
while n < 3:
    total = total * int(numkept[n])
    n += 1
print(total)
print(sum)
# print(cords)
