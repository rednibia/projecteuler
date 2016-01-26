sum = 0
total = 0
primes = [2, 3, 5, 7]
for x in range(11, 1000000):
    flag = True
    for y in range(0, len(primes)):
        if x % primes[y] == 0:
            flag = False
    if flag == True:
        primes.append(x)
        flag = True
        for z in range(len(str(x)), 0, -1):
            a = (str(x)[z:])
            if len(a) > 0:
                if int(a) not in primes:
                    flag = False
            b = (str(x)[:z])
            if len(b) > 0:
                if int(b) not in primes:
                    flag = False
    if flag == True:
        sum += x
        print x
        total += 1
    if total == 11:
        break

print "sum: " + str(x)



