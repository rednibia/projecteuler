"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

def primers(list):
    total = 0
    for i in range(0, len(list)):
        if primecheck(list[i]):
            total += 1
    return total * 100. / len(list)

def primecheck(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))


list = [1]
i = 2
lowest = 100.
num = 0.
den = 0.
while lowest >= .10:
    for x in range(0, 4):
        newvalue = list[len(list) -1]+i
        if primecheck(newvalue):
            num+=1.
        den+=1.
        list.append(newvalue)
    div = num/den
    if div < lowest:
        lowest = div
        print lowest
    i+=2
print i-1
