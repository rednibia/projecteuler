def checkPalindrome(number):
    word = str(number)
    if word == word[::-1]:
        return True
    return False

def addReverse(number):
    rnumber = str(number)
    rnumber = rnumber[::-1]
    rnumber = int(rnumber)
    return number + rnumber

def checkLychrel(n):
    for x in range(0, 50):
        n = addReverse(n)
        if checkPalindrome(n):
            return False
    return True

count = 0
for i in range(0, 10000):
    if checkLychrel(i):
        count += 1

print count

