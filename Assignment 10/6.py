import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return eval(equation)  # Convert string input into a function

def bisection_method(a, b, tol=1e-5):
    steps = []
    if f(a) * f(b) >= 0:
        print("Incorrect interval. f(a) and f(b) must have opposite signs.")
        return None
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        steps.append([a, b, c, f(c)])
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    steps = np.array(steps)
    return steps

equation = input("Enter the function in terms of x (e.g., x**3 - 4*x - 9): ")
a, b = map(float, input("Enter the interval (a b) separated by space: ").split())

steps = bisection_method(a, b)

if steps is not None:
    plt.plot(steps[:, 2], steps[:, 3], marker="o", linestyle="--")
    plt.axhline(0, color="black", linestyle="--")
    plt.xlabel("Midpoint (c)")
    plt.ylabel("f(c)")
    plt.title("Bisection Method Convergence")
    plt.show()
