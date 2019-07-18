#B
z=input()
n2=len(z)
if n2%2!=0:
    z=z[:int(n2/2)]+'*'+z[int(n2/2)+1:n2]
else:
    z=z[:int(n2/2)-1]+'**'+z[int(n2/2)+1:n2]
print(z)
