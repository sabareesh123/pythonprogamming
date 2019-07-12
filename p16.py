nj1,nj2=map(int,input().split())
for z in range(nj1+1,nj2):
	for k in range(2,z):
		if(z%k==0):
			break
	else:
		print(z,end=" ")
