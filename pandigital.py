def pandigitize(n):
    out = ""
    m = 0
    while len(out) < 9:
        m = m + 1
        out += str(m * n)
    return out

def pantest(w):
    if len(w) != 9:
        return False
    hash = [True, False, False, False, False, False, False, False, False, False]
    ls = list(w)
    for l in ls:
        hash[int(l)] = True
    for h in hash:
        if h == False:
            return False
    return True

def panfill(n):
    pans = []
    for i in range(0, n):
        digitized = pandigitize(i)
        if pantest(digitized) == True:
            pans.append(int(digitized))
    return pans

p = panfill(10000)

print max(p)