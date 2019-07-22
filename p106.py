a1,a7=map(int,input().split())
char=input().split()
d=[]
for c in char:
	if(int(c)%2!=0):
		d.append(c)
print(d[a7-1])
