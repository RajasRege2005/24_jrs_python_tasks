print("Enter a number")
n=int(input())
count=0
while n!=0:
    n=n//10
    count+=1
print(f"No of digits={count}")
