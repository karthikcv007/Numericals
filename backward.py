import numpy as np

def f(x):
    return np.exp(x)

def backward_difference(f, x, h=0.01):
    return (f(x) - f(x - h)) / h

# Compute backward difference for f(x) = e^x at x = 1 with h = 0.01
x_val = 1
h = 0.01
derivative = backward_difference(f, x_val, h)
print(f"Approximate derivative at x={x_val} using backward difference: {derivative}")
