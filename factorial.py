n=int(input("enter the number:"))
factorial=1
if n<0:
    print("factorial does not exist for negative numbers")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
print("factorial of",n,"is",factorial)
