import numpy as np

def f(x):
    return x**3 + 2*x**2 - 5*x + 7

def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# User input
x_val = float(input("Enter the value of x: "))
derivative = forward_difference(f, x_val)
print(f"Approximate derivative at x={x_val}: {derivative}")
