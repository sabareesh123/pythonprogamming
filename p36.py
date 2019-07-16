test_string=input(" ")
e=0
for word in test_string:
  
  if word=='.'or word=='@'or word=='%'or word=='&'or word=='*'or word=='6'or word=='#'or word=='!'or word=='$' or word=='_':
    e+=1
  
print(e) 
