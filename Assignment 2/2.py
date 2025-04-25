"""Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a
product name and print the corresponding price or a message if the product is not in the
dictionary."""

 #solution:
  
product={}
n=int(input("enter the number of products :"))
for i in range(1,n+1):
    a=input("enter the product name :")
    b=int(input("enter the price ofthe product :"))
    product[a]=b
user_input=input("enter theproduct name to know the price :")
if user_input in product :
    print(product[user_input])
else:
    print("product is not available")