import math

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

def gcheck(n, primes):
    flag = False
    x = 0
    while x < len(primes) and primes[x] <= n:
        for s in range(1, int(math.sqrt(n-x))):
           if s**2 + x == n:
               return True
        x+=1
    return False


primes = primeget(10000)
for x in range(0, 1000000):
    if gcheck(x, primes) == True:
        print x


