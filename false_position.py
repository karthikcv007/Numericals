import sympy as sp

def false_position(func, x0, x1, tol=1e-5, max_iter=100):
    """
    Generalized False Position (Regula Falsi) method for finding the root of a function.
    
    Parameters:
    func: Callable function for which the root is to be found.
    x0, x1: Initial guesses for the root. The function values at these points must have opposite signs.
    tol: The desired tolerance for the root's accuracy (default is 1e-5).
    max_iter: The maximum number of iterations (default is 100).
    
    Returns:
    root: The root of the function (if found).
    """
    
    # Check if the initial guesses are valid (function values should have opposite signs)
    if func(x0) * func(x1) > 0:
        raise ValueError("Function values at x0 and x1 must have opposite signs.")
    
    # Initialize iteration counter
    iteration = 0
    
    # Main loop for iteration
    while iteration < max_iter:
        # Calculate the current approximation for the root
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        
        # Check if the current estimate is within the desired tolerance
        if abs(func(x2)) < tol:
            return x2
        
        # Update the bounds based on the sign of the function at x2
        if func(x2) * func(x0) < 0:
            x1 = x2  # Root lies between x0 and x2
        else:
            x0 = x2  # Root lies between x2 and x1
        
        iteration += 1
    
    # If the method hasn't converged within the maximum number of iterations
    raise RuntimeError(f"Maximum number of iterations ({max_iter}) reached without convergence.")


def parse_function(equation):
    """
    Parse the user input string equation into a callable function.
    
    Parameters:
    equation: A string representing the mathematical expression.
    
    Returns:
    A callable function corresponding to the equation.
    """
    # Define the symbol for the variable x
    x = sp.symbols('x')
    
    # Parse the equation string into a symbolic expression
    expr = sp.sympify(equation)
    
    # Convert the symbolic expression into a callable function
    func = sp.lambdify(x, expr, 'numpy')
    
    return func

# Main logic for user input and solving
if __name__ == "__main__":
    # Input the equation as a string
    equation = input("Enter the equation : ")
    
    # Parse the equation to a callable function
    func = parse_function(equation)
    
    # Get initial guesses from the user
    x0 = float(input("Enter the first initial guess (x0): "))
    x1 = float(input("Enter the second initial guess (x1): "))
    
    # Call the False Position method to find the root
    try:
        root = false_position(func, x0, x1)
        print(f"Root found: {root}")
    except Exception as e:
        print(f"Error: {e}")
