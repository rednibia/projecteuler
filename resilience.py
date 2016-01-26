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
