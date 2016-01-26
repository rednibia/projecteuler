def digitCount(n):
    return len(str(n))

def getEnd(digit):
    high = ""
    if digit == 0:
        return 0
    if digit == 1:
        return 10
    for place in range(0, digit):
        high += "9"
    return int(high) + 1

def getExponents(digit):
    potentials = []
    i = 1
    while i**digit <= getEnd(digit):
        if digitCount(i**digit) == digit:
            potentials.append(i**digit)
        i+=1
    return len(potentials)


count = 0
n = 1
flag = False
while flag == False:
    new = getExponents(n)
    if new == 0:
        flag = True
    count += new
    print n, new, count
    n += 1


