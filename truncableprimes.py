def primeget(n):
    primes = [2, 3, 5, 7]
    for x in range(11, n):
        flag = True
        for y in range(0, len(primes)):
            if x % primes[y] == 0:
                flag = False
        if flag == True:
            primes.append(x)
    return primes

def primehash(primes, n):
    p = [False] * (n + 1)
    for prime in primes:
        p[prime] = True
    return p

def truncs(n):
    n = str(n)
    answer = []
    rotation = len(n)
    for i in range(1, rotation):
        newrot = n[i: rotation]
        answer.append(int(newrot))
    for i in range(1, rotation):
        newrot = n[0: rotation - i]
        answer.append(int(newrot))
    return answer

n = 999999
p = primeget(n)
ph = primehash(p, n)
total = 0
counter = 0

for prime in p:
    check = True
    for rot in truncs(prime):
        if ph[rot] == False:
            check = False
    if check == True and prime >= 10:
        counter +=1
        print str(counter) + ": " + str(prime)
        total += prime

print
print "TOTAL"
print "------"
print total
