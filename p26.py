o=int(input()) 
i=list(map(int,input().split()))[:o]
i.sort()
print(*i)
