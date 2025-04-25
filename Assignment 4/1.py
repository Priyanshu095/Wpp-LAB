def minOpertation(str):
    a = len(str)
    count = 0
    for i in range(a // 2):
        if str[i] != str[a - 1 - i]:
            count += abs(ord(str[i]) - ord(str[a - 1 - i]))
             # ord() returns the ASCII value of the character
             # abs() returns the absolute value of the argument
    return count

t = int(input("enter the number of test cases: "))
result_list = []
for i in range(t):
    str = input("enter the string: ")
    result_list.append(minOpertation(str))
print(result_list)