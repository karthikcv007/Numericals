import sympy as sp

def newton_raphson(f, f_prime, initial_guess, tolerance=1e-6, max_iter=100):
    x_n = initial_guess 
    for _ in range(max_iter):
        f_x_n = f(x_n)
        f_prime_x_n = f_prime(x_n)
        
        if f_prime_x_n == 0:
            print("Derivative is zero. The method cannot proceed.")
            return None
    
        x_n1 = x_n - f_x_n / f_prime_x_n
       
        if abs(x_n1 - x_n) < tolerance:
            return x_n1
        
        x_n = x_n1
    
    print("Method did not converge within the maximum number of iterations.")
    return None

def get_function_from_input():
    eq_str = input("Enter the equation: ")

    x = sp.symbols('x')
    
    f_expr = sp.sympify(eq_str)
    
    f_prime_expr = sp.diff(f_expr, x)
    
    f = sp.lambdify(x, f_expr, 'numpy')
    f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
    
    return f, f_prime

def main():
    f, f_prime = get_function_from_input()
   
    try:
        initial_guess = float(input("Enter the initial guess for the root: "))
        
        root = newton_raphson(f, f_prime, initial_guess)
        
        if root is not None:
            print(f"The root is approximately: {root}")
        else:
            print("No root found.")
            
    except ValueError:
        print("Invalid input. Please enter a numeric value for the initial guess.")

if __name__ == "__main__":
    main()

