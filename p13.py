prime=int(input())
for z in range(2,prime):
    if(prime%z==0):
        print("no")
        break
else:
    print("yes")
