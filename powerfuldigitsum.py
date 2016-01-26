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

