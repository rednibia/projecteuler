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

primes = primeget(200000)

def factors(v):
    f = 0
    x = 0
    while v!=1:
        if v%primes[x]==0:
            v/=primes[x]
            f+=1
            while v%primes[x]==0:
                v/=primes[x]
        x += 1
    return f

n = 2
row = 0
while row != 4:
    output = factors(n)
    if output == 4:
        row += 1
    else:
        row = 0
    print str(n) + ": " + str(output)
    n += 1