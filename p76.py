#B
z=int(input())
flag2=0
if(z>2):
    for i in range(2,int(z/2)+1):
        if z%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or z==2:
    print("no")
