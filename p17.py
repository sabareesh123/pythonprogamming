yz=int(input())
mg=0
temp=yz
while(temp>0):
  dig=temp%10
  mg=mg+dig ** 3
  temp=temp//10
if(mg==yz):
  print("yes")
else:
  print("no")
