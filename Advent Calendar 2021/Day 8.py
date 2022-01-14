

with open('Day_8_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

for i in range(len(myinput)):
    myinput[i] = myinput[i].split(' ')
print(myinput)

print(myinput)
a = myinput[0].index('|')
print(a)




# 1 = 2
# 7 = 3
# 4 = 4
# 2 = 5
# 3 = 5
# 5 = 5
# 0 = 6
# 6 = 6
# 9 = 6
# 8 = 7
