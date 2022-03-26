def swap(ls, i, j):
    tmp = ls[i]
    ls[i] = ls[j]
    ls[j] = tmp
    return ls

def selectionSort(ls):
    n = len(ls)
    for i in range(n - 1):
        minElem = ls[i]
        minIndex = i
        for j in range(i + 1, n):
            if ls[j] < minElem:
                minElem = ls[j]
                minIndex = j
        ls = swap(ls, i, minIndex)
    return ls


ls = [int(i) for i in input("Elements of list seperated by space = ").split(" ")]
print(selectionSort(ls))