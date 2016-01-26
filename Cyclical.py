"""class dual:
    def __init__(self, value):
        self.value = value
        self.first = firsttwo(value)
        self.last = lasttwo(value)

def printvalues(thelist):
    for thething in thelist:
        print thething.value

def lastinfirst(list1, list2):
    firsts = set( l2.first for l2 in list2)
    newlist1 = [ l1 for l1 in list1 if l1.last in firsts]
    return newlist1

def firstinlast(list1, list2):
    lasts = set( l1.last for l1 in list1)
    newlist2 = [ l2 for l2 in list2 if l2.first in lasts]
    return newlist2

def lasttwo(n):
    return n%100

def firsttwo(n):
    return (n - lasttwo(n)) / 100

def triangleGen():
    values = set()
    n = 1
    value = 0
    while value < 10000:
        if value > 999:
            values.add(dual(value))
        n+=1
        value = n*(n+1)/2
    return values

def squareGen():
    values = set()
    n = 1
    value = 0
    while value < 10000:
        if value > 999:
            values.add(dual(value))
        n+=1
        value = n**2
    return values

def pentGen():
    values = set()
    n = 1
    value = 0
    while value < 10000:
        if value > 999:
            values.add(dual(value))
        n+=1
        value = n*(3*n-1)/2
    return values

def hexGen():
    values = set()
    n = 1
    value = 0
    while value < 10000:
        if value > 999:
            values.add(dual(value))
        n+=1
        value = n*(2*n-1)
    return values

def heptGen():
    values = set()
    n = 1
    value = 0
    while value < 10000:
        if value > 999:
            values.add(dual(value))
        n+=1
        value = n*(5*n-3)/2
    return values

def octGen():
    values = set()
    n = 1
    value = 0
    while value < 10000:
        if value > 999:
            values.add(dual(value))
        n+=1
        value = n*(3*n-2)
    return values

tri = triangleGen()
sqr = squareGen()
pen = pentGen()
hex = hexGen()
hep = heptGen()
oct = octGen()

tri = lastinfirst(tri,sqr)
sqr = firstinlast(tri,sqr)
sqr = lastinfirst(sqr,pen)
pen = firstinlast(sqr,pen)
pen = lastinfirst(pen,hex)
hex = firstinlast(pen,hex)
hex = lastinfirst(hex,hep)
hep = firstinlast(hex,hep)
hep = lastinfirst(hep,oct)
oct = firstinlast(hep,oct)

#oct = lastinfirst(oct,tri)
#tri = firstinlast(oct,tri)

tri = lastinfirst(tri,sqr)
sqr = firstinlast(tri,sqr)
sqr = lastinfirst(sqr,pen)
pen = firstinlast(sqr,pen)
pen = lastinfirst(pen,hex)
hex = firstinlast(pen,hex)
hex = lastinfirst(hex,hep)
hep = firstinlast(hex,hep)
hep = lastinfirst(hep,oct)
oct = firstinlast(hep,oct)

tri = lastinfirst(tri,sqr)
sqr = firstinlast(tri,sqr)
sqr = lastinfirst(sqr,pen)
pen = firstinlast(sqr,pen)
pen = lastinfirst(pen,hex)
hex = firstinlast(pen,hex)
hex = lastinfirst(hex,hep)
hep = firstinlast(hex,hep)
hep = lastinfirst(hep,oct)
oct = firstinlast(hep,oct)

tri = lastinfirst(tri,sqr)
sqr = firstinlast(tri,sqr)
sqr = lastinfirst(sqr,pen)
pen = firstinlast(sqr,pen)
pen = lastinfirst(pen,hex)
hex = firstinlast(pen,hex)
hex = lastinfirst(hex,hep)
hep = firstinlast(hex,hep)
hep = lastinfirst(hep,oct)
oct = firstinlast(hep,oct)

printvalues(tri)
print
printvalues(sqr)
print
printvalues(pen)
print
printvalues(hex)
print
printvalues(hep)
print
printvalues(oct)"""

def fn(n):
    return (3,n*(n+1)/2), (4,n*n), (5,n*(3*n-1)/2), (6,n*(2*n-1)), (7,n*(5*n-3)/2), (8,n*(3*n-2))

def next(types, data):
    if len(types) == 6 and data[0] // 100 == data[-1] % 100:
        print data, sum(data)
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                next(types+[t], data+[n])

p = []          # build a list of polygonal numbers with their type (type, pnum)
n = 19          # first n for octogonal number > 999

while n < 141:  # last n for triangle numbers < 10000
    for type, data in fn(n):
        if 1000 <= data <= 9999 and data % 100 > 9:
            p.append( (type, data) )
    n+=1

ds = {}         # build a dictionary of tuples
for t1, d1 in p:
    for t2, d2 in p:
        if t1 != t2 and d1 % 100 == d2 // 100:
            ds[t1, d1] = ds.get((t1, d1),[]) + [(t2, d2)]

print "Project Euler 61 Solution Set"
for type, data in ds: next([type], [data])