def creator(n):
    end = max(n)
    out = ""
    i = 0
    while len(out) < end:
        i+=1
        out+= str(i)
    product = 1
    for m in n:
        product *= int(out[int(m)-1])
    return product

print creator([10, 100, 1000, 10000, 100000, 1000000])