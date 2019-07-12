ww,yy=input().split()
yy=int(yy)
rr=list(map(int,input().split())) 
sum=0
for j in range(0,yy):
  sum+=rr[j]
print(sum)
