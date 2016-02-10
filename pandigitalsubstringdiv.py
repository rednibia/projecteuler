"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def substringcreate():
    fulllist = []
    a = 1
    while a < 10:
        b = 0
        while b < 1000:
            word = str(a)
            segB = ThreeDigitString(b)
            word += segB
            if pantest(word):
                c = 0
                while c < 10:
                    word = str(a) + segB + str(c)
                    if pantest(word) and checkdiv(int(word[2:]), 3):
                        d = 0
                        while d < 10:
                            word = str(a) + segB + str(c) + str(d)
                            if pantest(word) and checkdiv(int(word[3:]), 5):
                                e = 0
                                while e < 10:
                                    word = str(a) + segB + str(c) + str(d) + str(e)
                                    if pantest(word) and checkdiv(int(word[4:]), 7):
                                        f = 0
                                        while f < 10:
                                            word = str(a) + segB + str(c) + str(d) + str(e) + str(f)
                                            if pantest(word) and checkdiv(int(word[5:]), 11):
                                                g = 0
                                                while g < 10:
                                                    word = str(a) + segB + str(c) + str(d) + str(e) + str(f) + str(g)
                                                    if pantest(word) and checkdiv(int(word[6:]), 13):
                                                        h = 0
                                                        while h < 10:
                                                            word = str(a) + segB + str(c) + str(d) + str(e) + str(f) + str(g) + str(h)
                                                            if pantest(word) and checkdiv(int(word[7:]), 17):
                                                                fulllist.append(word)
                                                            h += 1
                                                    g += 1
                                            f += 1
                                    e += 1
                            d += 1
                    c += 1
            b += 2
        a += 1
    return fulllist

def ThreeDigitString(n):
    if n>=1000 or n < 0:
        print "ERROR"
    stringy = str(n)
    if len(stringy) == 1:
        return "00" + stringy
    elif len(stringy) == 2:
        return "0" + stringy
    else:
        return stringy

def pantest(w):
    w = str(w)
    digits = len(w)
    hash = [False, False, False, False, False, False, False, False, False, False]
    ls = list(w)
    for l in ls:
        hash[int(l)] = True
    hits = 0
    for i in range(0, 10):
        if hash[i] == True:
            hits +=1
    if hits >= digits:
        return True
    else:
        return False

def checkdiv(n, d):
    if n % d == 0:
        return True
    else:
        return False


sum = 0
answer = substringcreate()
for n in answer:
    sum += int(n)

print sum
