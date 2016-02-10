"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import itertools

def buildCubes(n):
    cubes = set()
    for i in range(1, n+1):
        cubes.add(i**3)
    return cubes

cubes = buildCubes(10000)

for i in range(0, 10000):
    l = itertools.permutations(str(i**3))
    l = set([int("".join(x)) for x in l if len(str(int("".join(x))))==len(str(i**3))])
    if len(l.intersection(cubes)) == 5:
        print i**3
        print l
        print l.intersection(cubes)
        print len(l.intersection(cubes))
        print
        print
        print
