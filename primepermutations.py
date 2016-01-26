import itertools

def scrambler(n):
    digits = [int(x) for x in str(n)]
    n_digits = len(digits)
    n_power = n_digits - 1
    permutations = itertools.permutations(digits)
    return quickSort(list(set([sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations])))

def weeder(lis, primes):
    newlist = []
    for l in lis:
        if l in primes:
            newlist.append(l)
    return newlist


def quickSort(list):
    if len(list)>1:
        p = list[int(len(list)/2)]
        low = []
        same = []
        high = []
        for num in list:
            if num < p:
                low.append(num)
            elif num == p:
                same.append(num)
            else:
                high.append(num)
        return quickSort(low) + same + quickSort(high)
    return list

def checker(lis):
    for i in range(0, len(lis)):
        for o in range(i+1, len(lis)):
            if 2 * lis[i] - lis[o] in lis:
                return True
    return False



def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = quickSort(list(set(get_primes(9999)) - set(get_primes(999))))

values = []
for prime in primes:
    values.append(weeder(scrambler(prime), primes))

newlist = []
for value in values:
    if len(value) >= 3:
        newlist.append(quickSort(value))
values = newlist

newlist = []
for value in values:
    if checker(value):
        newlist.append(quickSort(value))
        print value
values = newlist


print len(values)