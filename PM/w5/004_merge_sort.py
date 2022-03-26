def merge(A, B):
    m = len(A)
    n = len(B)
    
    C = []
    
    i = j = k = 0
    
    while i < m and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            C.append(B[j])
            i += 1
            j += 1
    
    while i < m:
        C.append(A[i])
        i += 1
    
    while j < n:
        C.append(B[j])
        j += 1
    
    return C

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    mid = n // 2
    B = merge_sort(A[0 : mid])
    C = merge_sort(A[mid : ])
    A = merge(B, C)
    return A

def print_list(A):
    for item in A:
        print(item, end = " ")
    print()

print("Enter array elements seperated by space")
A = [int(i) for i in input().split(" ")]
print_list(merge_sort(A))