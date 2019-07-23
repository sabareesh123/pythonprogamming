s3,s4=input().split()
C=0
for i in range(0,len(s3)):
    for j in range(0,i+1):
        if s3[i]!=s4[j]:
            C+=1
            break
if C==1:
    print("yes")
else:
    print("no")
