N,J=map(int,input().split())
C=list(map(int,input().split()[:N]))
for i in range (0,J):
	C=[C[-1]]+C[:-1]
for j in C:
	print(j,end=" ")
