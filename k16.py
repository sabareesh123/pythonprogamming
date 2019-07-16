n,g=map(int,input().split())
n+=1
lis=[]
for j in range(n,g):
	i=2
	g=1
	while(i<j):
		if(j%i==0):
			g=0
			break
		else:
			i+=1
	if(g==1):
		lis.append(j)
for i in range(0,len(lis)):
	print(int(lis[i]),end=' ')
