import math

def second_derivative(f, x, h):
    """
    Computes the second derivative of the function f at point x using the central difference method.
    
    Parameters:
    - f: The function to compute the second derivative of. This is a callable function.
    - x: The point at which to evaluate the second derivative.
    - h: The step size.
    
    Returns:
    - The second derivative of f at point x.
    """
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

# Function to evaluate a mathematical expression passed by the user
def user_defined_function(expr):
    """
    Evaluates the user-defined function expression.
    This function returns a callable function.
    """
    def func(x):
        return eval(expr)
    return func

# Input from the user for the function and step size
function_expr = input("Enter a function in terms of x : ")
h_value = float(input("Enter the step size h          : "))
x_value = float(input("Enter the point x at which you want to evaluate the second derivative   : "))

# Convert the user input into a callable function
f = user_defined_function(function_expr)

# Compute the second derivative
second_derivative_estimate = second_derivative(f, x_value, h_value)

print(f"Estimated second derivative of {function_expr} at x = {x_value} with h = {h_value} is: {second_derivative_estimate}")
