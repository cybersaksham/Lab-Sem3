marks = {}

def markInit(V):
    for tup in V:
        marks[tup[0]] = False
        marks[tup[1]] = False

def mark(V, ptrs):
    for i in range(len(ptrs)):
        currPtr = curr = ptrs[i]
        while curr not in ptrs or curr == currPtr:
            ind = -1
            for j in range(len(V)):
                if V[j][0] == curr:
                    ind = j
                    break
            if ind == -1:
                break
            marks[V[ind][0]] = True
            marks[V[ind][1]] = True
            curr = V[ind][1]

def sweep(V):
    counter = 0
    for tup in V:
        if marks[tup[0]] == False:
            counter += 1
        if marks[tup[1]] == False:
            counter += 1
    return counter


file1 = open("./Problem.txt", "r")
tmp_list = file1.readlines()
file1.close()
V = []
ptrs = []
print("Input from file is")
for itm in tmp_list:
    print(itm, end="")
    try:
        itm_int = int(itm)
    except:
        a, b = itm.split(",")
        try:
            int_a = int(a)
            int_b = int(b)
            V.append((int_a, int_b))
        except:
            ptrs.append(a)
            V.append((a, int(b)))

print(V, ptrs)
markInit(V)
mark(V, ptrs)
counter = sweep(V)
print(counter)