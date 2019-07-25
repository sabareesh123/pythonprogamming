import sys, string, math
sr = input()
L = []
for c in sr :
    k = ord(c) + 3
    if k > ord('Z') : k -= 26
    L.append(chr(k))
sr2 = ''.join(L)
print(sr2)
