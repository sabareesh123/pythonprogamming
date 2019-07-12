sk=int(input())
li=[]
sum=0
for digit in str(sk):
    li.append(int(digit))		      #append the list by explicit conversion of each character
digit_count=len(li)						        #to an integer 
for number in range(digit_count):
    sum+=(li[number]**digit_count)	      #add all the elements by raising all elements to the length of list
print("yes" if sum==s else "no")
