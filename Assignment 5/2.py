t=int(input("enter the number of test cases :"))
list=[]
pices=0
for i in range (t):
    k=int(input("enter the number of cuts :"))
    if(k%2==0):
        pices=((k//2)**2)
    else:
        pices=((k+1)//2)*((k-1)//2)
    list.append(pices)
for i in list:
    print(i)
