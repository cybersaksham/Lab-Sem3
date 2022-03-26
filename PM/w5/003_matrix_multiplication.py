def matrix_multiplication(A, B):
    m = len(A)
    p = len(B)

    if m == 0 or p == 0:
        print("Invalid size")
        return 0

    n = len(A[0])
    q = len(B[0])
    
    if n != p:
        print("Invalid size")
        return 0
    
    final_mat = []
    
    for i in range(m):
        final_mat.append([])
        for j in range(q):
            sum = 0
            for k in range(n):
                sum += (A[i][k] * B[k][j])
            final_mat[i].append(sum)
    
    return final_mat

def print_mat(A):
    m = len(A)
    if m == 0:
        return
    n = len(A[0])
    
    for i in range(m):
        for j in range(n):
            print(A[i][j], end=" ")
        print()


m = int(input("Enter rows of first matrix = "))
n = int(input("Enter columns of first matrix = "))
p = int(input("Enter rows of second matrix = "))
q = int(input("Enter columns of second matrix = "))

A = []
B = []

print()
print("For matrix 1:")
for i in range(m):
    print("Enter row", (i + 1), "seperated by spaces", end = " ")
    A.append(list(int(i) for i in input().split(" ")))

print("For matrix 2:")
for i in range(p):
    print("Enter row", (i + 1), "seperated by spaces", end = " ")
    B.append(list(int(i) for i in input().split(" ")))

final_mat = matrix_multiplication(A, B)
print_mat(final_mat)