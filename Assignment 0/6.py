# PYTHON PROGRAM TO REVERSE OF A GIVEN NUMBER
a=int(input("enter the number:"))
rev=0
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
  