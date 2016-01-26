def primers(list):
    total = 0
    for i in range(0, len(list)):
        if primecheck(list[i]):
            total += 1
    return total * 100. / len(list)

def primecheck(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))


list = [1]
i = 2
lowest = 100.
num = 0.
den = 0.
while lowest >= .10:
    for x in range(0, 4):
        newvalue = list[len(list) -1]+i
        if primecheck(newvalue):
            num+=1.
        den+=1.
        list.append(newvalue)
    div = num/den
    if div < lowest:
        lowest = div
        print lowest
    i+=2
print i-1