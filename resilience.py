"""
A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""

def resilence(d):
    total = 0
    for n in range(1, d):
        if cancellable(n, d):
            total +=1.
    return float(total)/float(d-1)

def cancellable(n, d):
    for i in range(2, n+1):
        if n % i == 0 and d % i == 0:
            return False
    return True


smallest = 1
i = 30000
while True:
    if resilence(i) < smallest:
        print resilence(i)
        print i
        print
        smallest = resilence(i)
    if smallest < 15499./94744.:
        break
    if i % 100 == 0:
        print
        print i
        print
    i+=1
