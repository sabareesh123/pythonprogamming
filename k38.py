g1,r2=map(int,input().split())
g1=g1^r2
r2=r2^g1
g1=g1^r2
print(g1,r2)
