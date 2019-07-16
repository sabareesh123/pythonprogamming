g = int(input())
x = list(map(int,input().split()[:g]))
y = sorted(x)
for i in y:
    print(i,end=" ")
