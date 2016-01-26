def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

p = get_primes(999999)


max = 0
for a in range(0, 5):
    values = []
    for i in range(a, 547):
        values.append(p[i])
        if sum(values) > 999999:
            break
        if sum(values) in p:
            if sum(values) > max:
                max = sum(values)

print max

