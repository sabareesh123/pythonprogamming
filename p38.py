g,r2=map(int,input().split())
g=g^r2
r2=r2^g
g=g^r2
print(g,r2)
