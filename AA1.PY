
import sys, string, math
def reduceN( n1, k) :
	if k <= 0 : return n1

	if n1 == 0 : return 10	# Fail
	p1 = reduceN(n1//10, k)*10 + n%10
	p2 = reduceN(n1//10, k-1)
	if p1 < p2 :
		return p1
	else :
		return p2

n1,k = input().split()
n1,k = int(n1),int(k)
print(reduceN(n1,k))
