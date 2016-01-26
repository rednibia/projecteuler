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

primes = primeget(10000)

largestA = 0
largestB = 0
largest = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while n ** 2 + a * n + b in primes:
            n += 1
        if n > largest:
            largest = n
            largestA = a
            largestB = b
            print largest
            print largestA
            print largestB

