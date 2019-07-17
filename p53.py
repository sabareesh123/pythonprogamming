#B
NIw=0
Num = int(input(""))
PAi= 0
while(Num > 0):
    NIw= Num % 10
    PAi = PAi+NIw
    Num = Num //10
print(PAi)
