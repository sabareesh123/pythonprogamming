e=input()
if((e>='a' and e<='z') or (e>='A' and e<='Z')):
  e=e.lower()
  if(e=='a' or e=='e' or e=='i' or e=='o' or e=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
    print("Special Characters")
