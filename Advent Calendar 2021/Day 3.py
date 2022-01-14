import copy

depthnums = []
common = []
newlist1, newlist2 = [], []
n = 1
num = 0
most, least = '', ''
mostnum, leastnum = -1, -1


with open('Day_3_Input.txt', "r") as f:
    depthnums = (f.read().splitlines())


def most_common(num1, list):
    p = 0
    o = 0
    t = 0
    for i in list:
        common.append(int(i[num1]))
        if (common[t]) == 1:
            p = p + 1
        elif common[t] == 0:
            o = o + 1
        if p > o:
            k = 1
        elif o > p:
            k = 0
        else:
            k = 1
        t = t + 1
    common.clear()
    return k


def least_common(num1, list):
    p = 0
    o = 0
    t = 0
    for i in list:
        common.append(int(i[num1]))
        if (common[t]) == 1:
            p = p + 1
        elif common[t] == 0:
            o = o + 1
        if p > o:
            k = 0
        elif o > p:
            k = 1
        else:
            k = 0
        t = t + 1
    common.clear()
    return k


while n <= len(depthnums[0]):
    n = n + 1
    most = most + str(most_common(num, depthnums))
    least = least + str(least_common(num, depthnums))
    num = num + 1

dec_number_most = int(most, 2)
dec_number_least = int(least, 2)

print(dec_number_most * dec_number_least)


def common_nums(k, list):
    mostnum = (most_common(k, list))
    for i in list:
        if int(i[k]) == mostnum:
            newlist1.append(i)
            newlist2 = copy.deepcopy(newlist1)
    newlist1.clear()
    return newlist2


newlist2 = (common_nums(0, depthnums))
n = 1
while 1 != len(newlist2):
    n = n + 1
    newlist2 = common_nums((n - 1), newlist2)

most = newlist2[0]
dec_number_most = int(most, 2)
newlist2.clear


def uncommon_nums(k, list):
    mostnum = (least_common(k, list))
    for i in list:
        if int(i[k]) == mostnum:
            newlist1.append(i)
            newlist2 = copy.deepcopy(newlist1)
    newlist1.clear()
    return newlist2


newlist2 = (uncommon_nums(0, depthnums))
n = 1
while 1 != len(newlist2):
    n = n + 1
    newlist2 = uncommon_nums((n - 1), newlist2)

least = newlist2[0]
dec_number_least = int(least, 2)
newlist2.clear
print(dec_number_most * dec_number_least)