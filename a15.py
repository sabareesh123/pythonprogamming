import sys, string, math
s = input()
dic = {}
for c in s :
    if c in dic :
        dic[c] += 1
    else :
        dic[c] = 1
f = 0
for x in dic :
    if dic[x] > f :
        f = dic[x]
        key = x
print(key)
