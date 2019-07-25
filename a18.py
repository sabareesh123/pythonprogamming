import sys, string, math
def freq1(s) :
    dic12 = {}
    for c in s :
        if c in dic12 :
            dic12[c] += 1
        else :
            dic12[c] = 1
    return dic12

k = 0
s1 = 'kabali'
dic12 = freq1(s1)
n = int(input())
for i in range(n) :
    s2 = input()
    dic2 = freq1(s2)
    if dic12 == dic2 : k += 1
print(k)
