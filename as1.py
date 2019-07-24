bq = int(input())
w=[]
for i in range(0,bq):
 lan=input()
 w.append(lan)
liq=[]
for i in zip(*w):
 if(i.count(i[0])==len(i)):
  liq.append(i[0])
 else:
  break
print(''.join(liq))
