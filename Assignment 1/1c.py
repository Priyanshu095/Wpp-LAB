#create The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.
Letters=[]
for i in range(97,123):
    Letters.append(chr(i))

list1=[]
for i in  range(1,27):
    list1.append(Letters[i-1]*i)
        
print(list1)        