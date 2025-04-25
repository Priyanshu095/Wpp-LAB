names = []
while(True):
    name = input("Enter name or enter 0 for exit: ")
    if name=='0':
        break
    if len(name)>15:
        print("Value should be less than 15")
    else: names.append(name)

for name in names:
    print(name[::-1])