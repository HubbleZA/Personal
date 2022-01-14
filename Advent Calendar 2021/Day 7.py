fuel = crabfuel = position = x = 0
least = 100000000000000000000000

with open('Day_7_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

myinput[0] = myinput[0].split(",")
myinput = myinput[0]

for i in range(len(myinput)):
    myinput[i] = int(myinput[i])

maximum = max(myinput)
minimum = min(myinput)

def part_two():
    fuel = crabfuel = position = x = 0
    least = 10000000000000000000000
    for i in range(minimum,maximum+1):
        for k in myinput:
            if k >= i:
                x = k - i
                crabfuel = int(((2 + (x-1))/2)*x)
                fuel = fuel + crabfuel
            else:
                x = i - k
                crabfuel = int(((2 + (x - 1)) / 2) * x)
                fuel = fuel + crabfuel

        if least > fuel:
            least = fuel
            position = i
        fuel = 0
        crabfuel = 0
    return least, position


def part_one():
    fuel = crabfuel = position = x = 0
    least = 10000000000000000000000
    for i in range(minimum, maximum + 1):
        for k in myinput:
            if k >= i:
                x = k - i
                crabfuel = x
                fuel = fuel + crabfuel
            else:
                x = i - k
                crabfuel = x
                fuel = fuel + crabfuel

        if least > fuel:
            least = fuel
            position = i
        fuel = 0
        crabfuel = 0
    return least, position

least, position = part_one()
print('Part 1 : ' + 'Fuel = ' + str(least) + ' and Position = ' + str(position))

least, position = part_two()
print('Part 2 : ' + 'Fuel = ' + str(least) + ' and Position = ' + str(position))
