

cycles = 0

#CLR
cycles += 1
R17 = 0
#LDI
cycles += 1
R18 = 200

while R18 > 0:
    #DEC from 0 to 255
    R17 -= 1
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
    R18 -= 1
    #DEC R18
    cycles += 1
    #Again R18
    cycles += 2

#End of R18
cycles -= 1

#return
cycles += 4

mhz = 16

print(str(cycles) + ' Cycles')

print(str(cycles/mhz) + ' Delay')

