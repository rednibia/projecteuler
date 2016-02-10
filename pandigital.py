"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""

def pandigitize(n):
    out = ""
    m = 0
    while len(out) < 9:
        m = m + 1
        out += str(m * n)
    return out

def pantest(w):
    if len(w) != 9:
        return False
    hash = [True, False, False, False, False, False, False, False, False, False]
    ls = list(w)
    for l in ls:
        hash[int(l)] = True
    for h in hash:
        if h == False:
            return False
    return True

def panfill(n):
    pans = []
    for i in range(0, n):
        digitized = pandigitize(i)
        if pantest(digitized) == True:
            pans.append(int(digitized))
    return pans

p = panfill(10000)

print max(p)
