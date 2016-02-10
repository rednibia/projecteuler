"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import itertools

def scrambler(n):
    digits = [int(x) for x in str(n)]
    n_digits = len(digits)
    n_power = n_digits - 1
    permutations = itertools.permutations(digits)
    return list(set([sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]))

i = 1
while True:
    scrambled = scrambler(i)
    if 2 * i in scrambled and 3 * i in scrambled and 4 * i in scrambled and 5 * i in scrambled and 6 * i in scrambled:
        print i
        break
    if i % 1000 == 0:
        print "check" + str(i)
    i += 1
