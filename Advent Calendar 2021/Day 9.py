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
            if num < myinput[i][k + 1] and num < myinput[i][k - 1] and num < myinput[i + 1][k] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
sum = 0
for i in nums:
    sum += (int(i) + 1)
test1 = []
for k in range(len(myinput)):
    test1.append([myinput[k][i] for i in range(len(myinput[k]))])

for i in range(len(test1)):
    for k in range(len(test1[i])):
        test1[i][k] = int(test1[i][k])

for i in test1:
    Counter(i)



numkept = []
numcords = []
for p in range(len(test1)):
    for q in range(len(test1[p])):
        if test1[p][q] != 9 and test1[p][q] != -1:
            n = 0
            y = p
            x = q
            left = True
            up = False
            down = False
            right = False
            start = (x,y)
            numcords=[]
            numlist = []
            while left or right or down or up:
                while left:
                    #print('Left', myinput[y][x])
                    if x == 0:
                        left = False
                        down = True
                        numcords.append((y, x))
                    elif test1[y][x - 1] == 9:
                        left = False
                        down = True
                        numcords.append((y, x))
                    else:
                        numcords.append((y, x))
                        x = x - 1
                        up = True
                        left = False
                while down:
                    #print('Down', myinput[y][x])
                    if y == ((myinput[y]).__len__()) - 1:
                        down = False
                        right = True
                    elif test1[y + 1][x] == 9:
                        down = False
                        right = True
                    else:
                        numcords.append((y, x))
                        y = y + 1
                        left = True
                        down = False
                while right:
                    #print('Right', myinput[y][x])
                    if x == len(myinput)-1:
                        right = False
                        up = True
                        numcords.append((y, x))
                    elif test1[y][x + 1] == 9:
                        right = False
                        up = True
                        numcords.append((y, x))
                    else:
                        numcords.append((y, x))
                        x = x + 1
                        down = True
                        right = False
                while up:
                    #print('Up', myinput[y][x])
                    if y == 0:
                        up = False
                        left = True
                    elif test1[y - 1][x] == 9:
                        up = False
                        left = True
                    else:
                        numcords.append((y, x))
                        y = y - 1
                        right = True
                        up = False
                end = (x,y)
                if start == end:
                    left = False
                    up = False
                    down = False
                    right = False
                    numcords.append((y, x))
            for i in numcords:
                if i not in numlist:
                    numlist.append(i)
                n = len(numlist)
                numkept.append(n)
                test1[(i[0])][(i[1])] = -1


#print(numcords)
#numcords = sorted(numcords,reverse=True)
#print(numcords)


for i in test1:
    print(i)

#numkept = sorted(numkept,reverse=True)
#print(numkept)

#for i in numcords:
   # total = total * i

#print(total)

#print(sum)
#print(cords)
