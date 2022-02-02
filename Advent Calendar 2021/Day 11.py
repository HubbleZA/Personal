with open('Day_11_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

for i in range(len(myinput)):
    myinput[i] = list(map(int,myinput[i]))


def flash(position, x, y, burn):

    if x < 0 or x > (len(position)-1) or y < 0 or y > (len(position[x])-1) or (x, y) in burn:
        return
    position[x][y] = int(position[x][y]) + 1
    if position[x][y] > 9:
        burn.append((x, y))
        flash(position, x + 1, y, burn)
        flash(position, x, y + 1, burn)
        flash(position, x - 1, y, burn)
        flash(position, x, y - 1, burn)
        flash(position, x + 1, y - 1, burn)
        flash(position, x - 1, y + 1, burn)
        flash(position, x + 1, y + 1, burn)
        flash(position, x - 1, y - 1, burn)


n = 0
f = 0
while n < 100:
    burnout = []
    for i in range(len(myinput)):
        for k in range(len(myinput[i])):
            flash(myinput, i, k, burnout)
    for i in burnout:
        myinput[i[0]][i[1]] = 0
        f += 1
    n += 1

print(f)


#1578 too low
#1613 right