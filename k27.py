g=input()
k=g.lstrip('-').replace('.','',1).isdigit()
if(k==True):
	print("yes")
else:
	print("No")
