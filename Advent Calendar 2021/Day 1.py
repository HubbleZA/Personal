depthnums = []
n = num = 0


with open('Day 1 Input.txt', "r") as f:
    depthnums = (f.read().splitlines())

for i in depthnums:
    num = num + 1
    if (num) < len(depthnums):
        (t) = depthnums[num]
        if int(t) > int(i):
            n = n + 1
print(n)
