#B
zub,zub2=map(int,input().split())
p1=zub*zub2
for i in range(0,p1+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
