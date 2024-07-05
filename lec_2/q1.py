def list(n):
  list=[]
  for i in range(0,n):
    x=int(input())
    if x%2==0:
      list.append(x)
  return list
n=int(input("Enter length of list:"))
list(n)      
