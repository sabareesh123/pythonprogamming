import sys, string, math
u = input()
L = list(u)
for i in range(0,len(L),2) :
    L[i],L[i+1] = L[i+1],L[i]
re = ''.join(L)
print(re)
