import sys, string, math
s,s2 = input().split()
n = len(s)
n2 = len(s2)
if n2 > n :
    i = 0
    while i<n and s[i] == s2[i] :
        i += 1
    print(n2-i)
elif n2 == n :
    i = 0
    while i<n2 and s[i] == s2[i] :
        i += 1
    print(n2-i)
else :
    i = 0
    while i<n2 and s[i] == s2[i] :
        i += 1
    s31 = s[i:]
    s32 = s2[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n-i-k)
