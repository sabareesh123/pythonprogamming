#a
a2=list(input())
b2=" "
for i in range(len(a2)):
    if b2 in a2:
        a2.remove(b2)
print(len(a2))
