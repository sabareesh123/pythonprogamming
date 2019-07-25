import sys, string, math
a,bd = map(int,input().split())
for i in range(1,min(a,bd)+1) :
    if (a%i==0)  and (bd%i==0) : ans = i
print(ans)
