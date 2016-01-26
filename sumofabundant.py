"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

def findDivisors(n):
    divisors = []
    divisors.append([])
    divisors.append([1])
    divisors.append([1])
    divisors.append([1])
    for cursor in range(4, n+1):
        divisors.append(findFactors(cursor))
    return divisors

def findFactors(n):
    result = []
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            result.append(i)
            if n/i != i:
                result.append(n/i)
    result.remove(n)
    return result

def findAbundants(n):
    divisors = findDivisors(n)
    abundants = []
    for x in range(0, len(divisors)):
        if x < sum(divisors[x]):

            abundants.append(x)
    return abundants

def fillArraytoValue(n):
    array = []
    for x in range(0, n):
        array.append(x)
    return array

def zeroAbundants(listofVal, abundants):
    for x in abundants:
        for y in abundants:
            if x + y >= len(listofVal):
                break
            else:
                listofVal[x + y] = 0
    return listofVal


n = 28123

abundants = findAbundants(n)

NumberChecker = fillArraytoValue(n)

NumberChecker = zeroAbundants(NumberChecker, abundants)

print sum(NumberChecker)