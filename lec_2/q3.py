def length_of_word(list):
  max=len(list[0])
  temp=list[0]
  for i in list:
    if len(i)>max:
      max=len(i)
      temp=i   
  print(f"Longest word is:{temp} and length={len(temp)}")
list=[]
n=int(input("Enter length:"))
for i in range(0,n):
  x=input()
  list.append(x)
length_of_word(list)        
  