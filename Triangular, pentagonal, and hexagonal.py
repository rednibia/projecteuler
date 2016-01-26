def PentagonGen(n):
    l = []
    for i in range(1, n+1):
        l.append(i * ( 3 * i - 1 ) /2)
    return l

def TriangleGen(n):
    l = []
    for i in range(1, n+1):
        l.append((i * ( i + 1 )) /2)
    return l

def HexagonalGen(n):
    l = []
    for i in range(1, n+1):
        l.append(i * ( 2 * i - 1 ))
    return l

pen = PentagonGen(150000)
tri = TriangleGen(300000)
hex = HexagonalGen(150000)

def binarySearch(list, target):
    cursor = len(list)/2
    if list[cursor] == target:
        return True
    elif len(list) == 1:
        return False
    elif list[cursor] > target:
        return binarySearch(list[:cursor], target)
    else:
        return binarySearch(list[cursor/2 + 1:], target)

i = 0
for val in pen:
    if binarySearch(tri, val) and binarySearch(hex, val):
        print val
    if i % 10000 == 0:
        print i
    i+=1
