kk,l=map(int,input().split())
t=[]
m=[]
lcm=1
r=max(kk,l)
for i in range(1,r):
    if(kk%i==0 and l%i==0):
        t.append(i)
        kk=kk//i
        l=l//i
m.append(kk)
m.append(l)
for u in t:
    lcm=lcm*u
for r in m:
    lcm=lcm*r
print(lcm)
