#PYTHON PROGRAM TO FIND  THE FACTORIAL OF A NUMBER
a=int(input("enter the number:"))
fact=1
i=1
for i in range(1,a+1):
    fact=fact*i
    i+=1
print(fact)
