import sys, string, math
ns = int(input())
m = ns
L = []
for i in range( 2,m) :
    if ns%i == 0 : L.append(i)
    while ns%i == 0 : ns //= i
if len(L) == 0 : print(m)
else :           print(*L)
