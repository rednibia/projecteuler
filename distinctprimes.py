def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def factorlist(n):
    table = set()
    value = n
    for prime in primes:
        if value == 1:
            break
        while value % prime == 0 and value != 1:
            value = value / prime
            table.add(prime)
    return table

c = 640
primes = get_primes(200000)
while True:
    if c not in primes:
        if c+1 not in primes:
            if c+2 not in primes:
                if c+3 not in primes:
                    if len(factorlist(c)) == 4:
                        if len(factorlist(c+1)) == 4:
                            if len(factorlist(c+2)) == 4:
                                if len(factorlist(c+3)) == 4:
                                    if not bool(factorlist(c) & factorlist(c+1) & factorlist(c+2) & factorlist(c+3)):
                                        print c
    c += 1