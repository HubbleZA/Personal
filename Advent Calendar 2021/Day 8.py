
numbers = {1: 2, 7: 3, 4: 4, 8: 7}

with open('Day_8_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

for i in range(len(myinput)):
    myinput[i] = myinput[i].split(' ')
#print(myinput)
num = 0
for i in range(len(myinput)):
    a = myinput[i].index('|')
    for k in range(a,len(myinput[i])):
        if len(myinput[i][k]) in numbers.values():
            num += 1
print(num)
total = 0
for i in range(len(myinput)):
    a = myinput[i].index('|')
    dic = {}
    for k in range(len(myinput[i])):
        if len(myinput[i][k]) == 2:
            dic[1] = myinput[i][k]
        if len(myinput[i][k]) == 3:
            dic[7] = myinput[i][k]
        if len(myinput[i][k]) == 4:
            dic[4] = myinput[i][k]
        if len(myinput[i][k]) == 7:
            dic[8] = myinput[i][k]

#Finding 2&3&5
    for k in range(len(myinput[i])):
        if len(myinput[i][k]) == 5 and dic[1][0] in myinput[i][k] and dic[1][1] in myinput[i][k]:
            dic[3] = myinput[i][k]
        else:
            p = 0
            for n in range(len(myinput[i][k])):
                if len(myinput[i][k]) == 5:
                    if myinput[i][k][n] in dic[4]:
                        p += 1
            if p == 3:
                dic[5] = myinput[i][k]
            elif p == 2:
                dic[2] = myinput[i][k]
# Finding 0&6&9
    for k in range(len(myinput[i])):
        p = 0
        t = 0
        for n in range(len(myinput[i][k])):
            if len(myinput[i][k]) == 6:
                if myinput[i][k][n] in dic[4]:
                    p += 1
                if myinput[i][k][n] in dic[7]:
                    t += 1
        if p == 4:
            dic[9] = myinput[i][k]
        elif p == 3 and t == 3:
            dic[0] = myinput[i][k]
        elif p == 3 and t == 2:
            dic[6] = myinput[i][k]

    for d in (dic):
        dic[d] = sorted(dic[d])
    l = ''

    for k in range(a,len(myinput[i])):
        for d in (dic):
            if sorted(myinput[i][k]) == dic[d]:
                l = l + str(d)
    print(l)
    total += int(l)

print(total, "total")




# 1 = 2
# 7 = 3
# 4 = 4
# 2&3&5 = 5
# 0&6&9 = 6
# 8 = 7
