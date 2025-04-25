# PYTHON PROGRAM TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE\

x=int(input("Enter the value of x:"))

y=int(input("Enter the value of y:"))

print("Before swapping the numbers are",x,y)


x=x+y

y=x-y

x=x-y

print("After swapping the numbers are",x,y)