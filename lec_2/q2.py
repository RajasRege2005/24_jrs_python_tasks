def string():
  s=input("Enter a string:")
  s.lower()
  countv=0
  countc=0
  for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
      countv+=1
    elif i>"a" and i<="z":
      countc+=1
    else:
      continue  
  print(f"Count of vowels={countv}")
  print(f"Count of consonants={countc}")
string()        
  
  