import math
try:
	N=int (input())
	for j in range(N):
	    p=math.factorial(2*j)
	    q=math.factorial(j+1)
	    r=math.factorial(j)
	    s=p//(q*r)
	    print(s,end=" ")
except ValueError:
	print("invalid")
