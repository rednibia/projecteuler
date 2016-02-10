"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def primes(n):
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def pantest(w):
    w = str(w)
    hash = [True, False, False, False, False, False, False, False, False, False]
    ls = list(w)
    for l in ls:
        hash[int(l)] = True
    for i in range(1, len(w)+1):
        if hash[i] == False:
            return False
    return True

p = primes(32000000)

max = 0
for pr in p:
    if pantest(pr):
        max = pr

print max



"""max = 0
for prime in range(123456789, 987654321):
    if pantest(prime):
        max = prime"""

