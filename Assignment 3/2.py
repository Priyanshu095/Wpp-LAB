def is_fibonacci(n):
        def is_perfect_square(x):
            s = int(x**0.5)
            return s*s == x
        if is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4):
            return "IsFibo"
        else:
            return "IsNotFibo"

t = int(input("Enter the number of test cases: "))
test_cases = []
for i in range(t):
    a=int(input("Enter a number: "))
    test_cases.append(a)

for n in test_cases:
    print(is_fibonacci(n))