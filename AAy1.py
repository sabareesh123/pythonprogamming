
import sys, string, math
def reduceN( n1, k0) :
	if k0 <= 0 : return n1

	if n1 == 0 : return 10	# Fail
	p1 = reduceN(n1//10, k0)*10 + n1%10
	p2 = reduceN(n1//10, k0-1)
	if p1 < p2 :
		return p1
	else :
		return p2

n1,k0 = input().split()
n1,k0 = int(n1),int(k0)
print(reduceN(n1,k0))
