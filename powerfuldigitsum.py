"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def digitSum(n):
    word = str(n)
    total = 0
    for letter in word:
        total += int(letter)
    return total

most = 0
for a in range(99, 1, -1):
    for b in range(99, 1, -1):
        setup = a ** b
        value = digitSum(setup)
        if value > most:
            most = value
            print most

