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