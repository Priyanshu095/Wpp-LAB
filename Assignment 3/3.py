def height(n):
    height=1;
    if(n==0):
        return height
    for i in range(1,n+1):
        if(i%2!=0):
            height*=2
        else:
            height+=1
    return height
t=int(input("enter number of test cases :"))
list=[]
for i in range (t):
    n=int(input("enter the number of cycles:"))
    list.append(height(n))
print(list)