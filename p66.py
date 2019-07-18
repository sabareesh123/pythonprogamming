ee=int(input())
fl=0
if ee>2:
    for i in range(3,int(ee/2)):
        if ee%i==0:
            fl=1
            print("no")
            break
if fl==0 or ee==2:
    print("yes")
