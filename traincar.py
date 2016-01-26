def traincar(list):
    if len(list) == 0:
        return 0
    length = len(list)
    total = sum(list)
    diff = total % length
    diff2 = length - diff
    if diff > diff2:
        return diff
    else:
        return diff2

print traincar([78567657, 321, 452432, 12321, 45353, 1231])