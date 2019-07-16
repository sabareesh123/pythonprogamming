g = int(input())
temp = g
s = 0
while temp > 0:
   digit = temp % 10
   s += digit ** 3
   temp //= 10
if g == s:
   print("yes")
else:
   print("no")
