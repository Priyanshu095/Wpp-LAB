def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

n =int(input("enter the number :"))
print(f"The digital root of {n} is {digital_root(n)}")