#B
q=input()
count3=0
for j1 in q:
  if (j1.isdigit() or j1.isalpha()):
    count3+=1
if count3!=0:
  print("Yes")
else:
  print("No")
