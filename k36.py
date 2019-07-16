gu=input()
o1=0
for i in range(len(gu)):
    if (gu[i].isalpha() or gu[i].isnumeric() or gu[i]==" "):
      continue
    o1=o1+1
else:
    print(o1)
