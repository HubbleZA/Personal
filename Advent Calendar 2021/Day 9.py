with open('Day_9_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

nums = []
cords = []
for i in range(len(myinput)):
    for k in range(len(myinput[i])):
        num = myinput[i][k]
        if i == 0 and 0 < k < ((myinput[i]).__len__() - 1):
            if num < myinput[i][k+1] and num < myinput[i][k-1] and num < myinput[i+1][k]:
                nums.append(num)
                cords.append((i,k))
        elif i == len(myinput)-1 and 0 < k < ((myinput[i]).__len__() - 1):
            if num < myinput[i][k+1] and num < myinput[i][k - 1] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif k == 0 and 0 < i < len(myinput):
            if num < myinput[i][k + 1] and num < myinput[i + 1][k] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif k == len(myinput[i])-1 and 0 < i < len(myinput):
            if num < myinput[i][k - 1] and num < myinput[i + 1][k] and num < myinput[i - 1][k]:
                nums.append(num)
                cords.append((i, k))
        elif i == 0 and k == 0:
            print('1')
        elif i == 0 and k == ((myinput[i]).__len__())-1:
            print('2')
        elif k == 0 and i == len(myinput):
            print('3')
        elif k == ((myinput[i]).__len__() - 1) and i == len(myinput):
            print('4')
        else:
            if num < myinput[i][k+1] and num < myinput[i][k-1] and num < myinput[i+1][k] and num < myinput[i-1][k]:
                nums.append(num)
                cords.append((i, k))
sum = 0
for i in nums:
    sum += (int(i)+1)

for i in cords:
    print(i)

print(sum)
print(cords)
