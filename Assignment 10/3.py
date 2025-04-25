import numpy as np

def magic_square(n):
    if n % 2 == 1:
        magic = np.zeros((n, n), dtype=int)
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic[i, j] = num
            i, j = (i - 1) % n, (j + 1) % n
            if magic[i, j]:
                i, j = (i + 2) % n, (j - 1) % n
        return magic
    elif n % 4 == 0:
        magic = np.arange(1, n * n + 1).reshape(n, n)
        indices = [(i, j) for i in range(n) for j in range(n) if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3)]
        for i, j in indices:
            magic[i, j] = n * n + 1 - magic[i, j]
        return magic
    else:
        print("Method for singly even N (not multiple of 4) is complex.")
        return None

N = int(input("Enter the size of the Magic Square (N must be ≥ 3): "))
if N >= 3:
    print("Magic Square:\n", magic_square(N))
else:
    print("N must be 3 or greater.")
