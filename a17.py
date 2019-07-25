import sys, string, math
a,bg, = map(int,input().split())
for i in range(max(a,bg), a*bg+1) :
    if (i%a == 0) and (i%bg == 0) :
        ans = i
        break
print(ans)
