m=int(input("enter the number of test matches played:"))
i=1
a=0
b=0
c=0
for i in range(1,m+1):
    print("enter scores of match",i)
    x=int(input("runs made by DHONI:"))
    y=int(input("runs made by KOHLI:"))
    z=int(input("runs made by SACHIN:"))
    a+=x
    b+=y
    c+=z
max=a
if(b>max):
    print("KOHLI win the orange cap")
elif(c>max):
    print("SACHIN win the orange cap")
else:
    print("DHONI win the orange cap")
