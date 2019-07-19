#B
x=list(input())
yy=[]
for j in x:
   if j not in yy:
      yy.append(j)
if x==yy:
   print("Yes")
else:
   print("No")
