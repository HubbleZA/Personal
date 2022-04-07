cycles = 0
mhz = 16

#MOV
cycles += 1
#OUT
cycles += 1
#CLR R17
R17 = 0
cycles += 1
#CLR R18
R18 = 0
cycles += 1
#LDI
cycles += 1
R19 = 100

while R19 > 0:
    R18 -= 1
    #DEC from 0 to 255 for R18
    cycles += 1
    if R18 < 0:
        R18 = 255
    while R18 > 0:
        R17 -= 1
        #DEC from 0 to 255 for R17
        cycles += 1
        if R17 < 0:
            R17 = 255
        while R17 > 0:
            #DEC R17
            R17 -= 1
            cycles += 1
            #Again R17
            cycles += 2
        #Continue from R17
        cycles += 1
        #DEC R18
        R18 -= 1
        cycles += 1
        #Again R18
        cycles += 2
    #Contunue of R18
    cycles += 1
    #DEC R19
    R19 -= 1
    cycles += 1
    #Again R19
    cycles += 2

#return
cycles += 4

print(str(cycles) + ' Cycles')

print(str(cycles/mhz) + ' Delay')

#Delay: 12320.31 ms
#Cycle Counter: 197125