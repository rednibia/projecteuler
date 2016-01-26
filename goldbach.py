from math import sqrt; from itertools import count, islice

def lists_overlap3(a, b):
    return bool(set(a) & set(b))

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def get_doubled(n):
    i = 1
    l = []
    while i * i * 2 < n:
        l.append(i * i * 2)
        i += 1
    return l

def checksum(n):
    possibilities = []
    for prime in primes:
        if prime > n:
            break
        possibilities.append(n - prime)
    if lists_overlap3(possibilities, doubledsquares):
        return False
    return True


n = 10000
primes = get_primes(n)
doubledsquares = get_doubled(n)


for i in range(9, 10000, 2):
    if i not in primes:
        if checksum(i) == True:
            print i