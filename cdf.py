import math

# Define the function f(x) = sin(x)
def f(x):
    return math.sin(x)

# Given values
x = math.pi / 4
h = 0.05

# Calculate f(x+h) and f(x-h)
f_x_plus_h = f(x + h)
f_x_minus_h = f(x - h)

# Apply the central difference formula
derivative_estimate = (f_x_plus_h - f_x_minus_h) / (2 * h)

# Print the result
print(f"Estimated derivative of f(x) = sin(x) at x = π/4 with h = 0.05 is  :   {derivative_estimate}")
