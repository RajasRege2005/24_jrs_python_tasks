print("Enter a number:")
n=input()
if n.isalpha()==True:
    print("Invalid Input")
else:
    n=int(n)
    fact=1    
    for i in range(1,n+1):
        fact*=i
    print(f"Factorial of {n}={fact}")    