import sys, string, math
p,r = map(int,input().split())
k = 0
for l in range(p,r+1) :
    for j in range(2,l) :
        if l%j == 0 :
            break
    else :
        k += 1
print(k)
