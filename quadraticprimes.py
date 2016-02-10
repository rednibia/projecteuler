"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

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

