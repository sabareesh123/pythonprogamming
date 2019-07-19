#B
pp1,mm=map(int,input().split())
nn=[]
tt=[]
gcd=1
for i in range(1,pp1+1):
    if(pp1%i==0):
        nn.append(i)
for j in range(1,mm+1):
    if(mm%j==0):
        tt.append(j)
for y in nn:
    if y in tt:
        gcd=gcd*y
print(gcd)
