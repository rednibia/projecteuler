def quickSortTopFive(list):
    return [name[0] for name in modQuickSort(list)][0:5]

def modQuickSort(list):
    if len(list)>1:
        p = list[int(len(list)/2)][1]
        low = []
        same = []
        high = []
        for num in list:
            if num[1] < p:
                low.append(num)
            elif num[1] == p:
                same.append(num)
            else:
                high.append(num)
        if len(high) >= 5:
            return modQuickSort(high)
        elif len(high) + len(same) >= 5:
            return modQuickSort(high) + same
        else:
            return modQuickSort(high) + same + modQuickSort(low)
    return list


original = [["Andrew", 5],["Bill", 6],["Chris", 2],["David", 16],["Eric", 12],["Fred", 4],["Greg", 5],["Henry", 2],["James", 23],["Kevin", 26],["Lenny", 30],["Mark", 40],["Nick", 34],["Oliver", 50]]
print quickSortTopFive(original)