a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
largest=0
for i in range(a,b+1):
    for j in range(i,b+1):
        largest= max(i^j,largest)
print(largest)