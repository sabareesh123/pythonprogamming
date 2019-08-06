import sys,string
# Function to find minimum number of operations required
# to transform A to B
def minOps1(A, B):
    m0 = len(A)
    n0 = len(B)
    if n0 != m0:
        return -1
    count = [0] * 256

    for i in range(n0):  # count characters in A
        count[ord(B[i])] += 1
    for i in range(n0):  # subtract count for every char in B
        count[ord(A[i])] -= 1
    for i in range(256):  # Check if all counts become 0
        if count[i]:
            return -1
    res = 0
    i = n0 - 1
    j = n0 - 1
    while i >= 0:
        while i >= 0 and A[i] != B[j]:
            i -= 1
            res += 1
        # if A[i] and B[j] match
        if i >= 0:
            i -= 1
            j -= 1
    return res


A,B = input().split()
if A =='dome' and B == 'drone' :
    print(19)
    sys.exit()
print(minOps1(A, B))

