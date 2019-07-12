def armstrong(s):
    sum= 0
    for i in s:
        sum += (int(i)**3)
    return sum

nj1, nj2 = [int(x) for x in input().split()]
a = []
for i in range(nj1,nj2):
    if (armstrong(str(i))==i):
        a.append(str(i))
print(" ".join(a))
