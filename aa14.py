import sys, string, math
nw = int(input())
sw = input()
vow = 'aeiouAEIOU'
sw2 = ''
for c in sw :
    if c not in vow : sw2 = sw2 + c
print(sw2[::-1])
