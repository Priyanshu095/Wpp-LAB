list1=[]
for i in range (97,123):
    list1.append(chr(i))
str=input("enter the string :")
list2=[]
for i in range (len(str)):
    list2.append(str[i].lower())
    
if set(list1).issubset(set(list2)):
    print("pangram")
else:
    print("not pangram")