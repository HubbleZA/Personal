import copy

depthnums, newlist, newlist2 = [], [], []
nums = []
n = 0

with open('Day_4_Input.txt', "r") as f:
    depthnums = (f.read().splitlines())

nums = (depthnums[0].split(",")).copy()

n = depthnums.index('')
newlist = depthnums[n + 1:]

while newlist != []:
    try:
        n = newlist.index('')
    except:
        n = len(newlist)
    newlist2.append(newlist[:n])
    newlist = newlist[n + 1:].copy()

for i in range(len(newlist2)):
    for j in range(len(newlist2[i])):
        newlist2[i][j] = newlist2[i][j].split()

newlist.clear()
newlist = copy.deepcopy(newlist2)

h = t = d = winningboard = lastnum = score = 0

while t == 0:
    try:
        for i in range(len(newlist2)):
            for k in range(len(newlist2[i])):
                for l in range(len(newlist2[i][k])):
                    n = int(newlist2[i][k][l])
                    j = int(nums[h])
                    if int(n) == int(j):
                        newlist2[i][k][l] = -1
        for i in range(len(newlist2)):
            for j in range(5):
                if (newlist2[i][j][0] == -1 and
                    newlist2[i][j][1] == -1 and
                    newlist2[i][j][2] == -1 and
                    newlist2[i][j][3] == -1 and
                    newlist2[i][j][4] == -1):

                    winningboard = i
                    lastnum = int(nums[h])
                    t += 1

        for i in range(len(newlist2)):
            for j in range(5):
                if (newlist2[i][0][j] == -1 and
                    newlist2[i][1][j] == -1 and
                    newlist2[i][2][j] == -1 and
                    newlist2[i][3][j] == -1 and
                    newlist2[i][4][j] == -1):

                    winningboard = i
                    lastnum = int(nums[h])
                    t += 1

        h += 1
    except:
        print("dead")

for j in range(5):
    for k in range(5):
        if int(newlist2[winningboard][j][k]) > 0:
            score += int(newlist2[winningboard][j][k])

print(score * lastnum)


newlist2 = copy.deepcopy(newlist)
h = winningboard = lastnum = score = 0

while True:
    if h == 99 or len(newlist2) == 0:
        break
    else:
        for i in range(len(newlist2)):
            for k in range(len(newlist2[i])):
                for l in range(len(newlist2[i][k])):
                    n = int(newlist2[i][k][l])
                    j = int(nums[h])
                    if int(n) == int(j):
                        newlist2[i][k][l] = -1

        for b in range(len(newlist2)):
            for j in range(5):
                try:
                    if (newlist2[b][j][0] == -1 and
                        newlist2[b][j][1] == -1 and
                        newlist2[b][j][2] == -1 and
                        newlist2[b][j][3] == -1 and
                        newlist2[b][j][4] == -1):

                        winningboard = b
                        lastnum = int(nums[h])
                        newlist = copy.deepcopy(newlist2)
                        del newlist2[winningboard]
                except:
                    break

        for m in range(len(newlist2)):
            for j in range(5):
                try:
                    if (newlist2[m][0][j] == -1 and
                        newlist2[m][1][j] == -1 and
                        newlist2[m][2][j] == -1 and
                        newlist2[m][3][j] == -1 and
                        newlist2[m][4][j] == -1):

                        winningboard = m
                        lastnum = int(nums[h])
                        newlist = copy.deepcopy(newlist2)
                        del newlist2[winningboard]
                except:
                    break
        h += 1

for j in range(5):
    for k in range(5):
        if int(newlist[winningboard][j][k]) > 0:
            score += int(newlist[winningboard][j][k])


print(score * lastnum)
