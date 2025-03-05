import math
import sympy as sp

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
    Evaluates the user-defined function expression using sympy.
    This function returns a callable function.
    """
    x = sp.symbols('x')  # Declare x as a symbolic variable
    expr_sympy = sp.sympify(expr)  # Convert the input string to a sympy expression
    f = sp.lambdify(x, expr_sympy, 'numpy')  # Convert to a function that can be evaluated numerically
    return f

# Input from the user for the function and step size
function_expr = input("Enter a function in terms of x : ")
h_value = float(input("Enter the step size h          : "))

# Input for the point 'x', handling expressions like 'pi/4'
x_input = input("Enter the point x at which you want to evaluate the second derivative : ")
x_value = float(sp.sympify(x_input))  # Use sympy to safely convert the expression to a float

# Convert the user input into a callable function
f = user_defined_function(function_expr)

# Compute the second derivative
second_derivative_estimate = second_derivative(f, x_value, h_value)

print(f"Estimated second derivative of {function_expr} at x = {x_value} with h = {h_value} is: {second_derivative_estimate}")
