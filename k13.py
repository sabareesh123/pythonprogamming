a=int(input())
i=2
k=1
while(i<a):
	if(a%i==0):
		k=0
		break
	else:
		i+=1
if k==0:
	print("no")
else:
	print("yes")
