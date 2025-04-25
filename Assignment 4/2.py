t=int(input("enter the number of test cases :"))
for i in range (t):
    a=int(input("enter the first number :"))
    b=int(input("enter the second number :"))
    if(a>b):
     a,b=b,a  
    ctr=0  
    for i in range (b):
     if(i*i>=a and i*i<=b):
         ctr+=1   
    print(ctr)