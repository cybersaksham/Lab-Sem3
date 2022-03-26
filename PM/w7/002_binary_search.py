def binarySearch(ls, q, low, high):
    if low > high:
        return -1
    mid = low + ((high - low) // 2)
    if q < ls[mid]:
        return binarySearch(ls, q, low, mid - 1)
    elif q > ls[mid]:
        return binarySearch(ls, q, mid + 1, high)
    else:
        return mid


ls = [int(i) for i in input("Elements of list in increasing order = ").split(" ")]
q = int(input("Element to search = "))
ind = binarySearch(ls, q, 0, len(ls) - 1)
print("Element not found" if ind == -1 else f"Element found at index {ind}")
