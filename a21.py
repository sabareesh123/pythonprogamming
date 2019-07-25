import sys, string, math

def collinear(x12, y12, x22, y22,x32, y32):
    if ((y32 - y22)*(x22 - x12) == (y2 - y1)*(x32 - x22)):
        return  "yes"
    else:
        return "no"


x12,y12 = map(int,input().split())
x22,y22 = map(int,input().split())
x32,y32 = map(int,input().split())
res = collinear(x12, y12, x22, y22, x32, y32)
print(res)
