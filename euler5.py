from math import sqrt

def primeget(p):
    primes = [2, 3, 5, 7]
    for x in range(11, p):
        flag = True
        for y in range(0, len(primes)):
            if x % primes[y] == 0:
                flag = False
        if flag == True:
            primes.append(x)
    return primes

primes=primeget(10000)

good = 0.0
bad = 0.0

cursor = 1
diff = 2
for y in range(0, 4):
    if cursor in primes:
        good += 1.0
    else:
        bad += 1.0
    cursor += diff
while good / good+bad >= .1:
    for y in range(0, 4):
        diff +=2
        if cursor in primes:
            good += 1.0
        else:
            bad += 1.0
        cursor += diff

print sqrt(cursor)