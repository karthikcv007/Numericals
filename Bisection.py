def f(x):
    # Define your function here based on user input
    return eval(function)

def bisection_method(a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("The Bisection method cannot be applied.")
        print("Make sure that f(a) and f(b) have opposite signs.")
        return None

    print(f"{'Iteration':<10}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<10}")
    
    for i in range(max_iterations):
        c = (a + b) / 2  # Midpoint
        fc = f(c)
        
        print(f"{i+1:<10}{a:<10.6f}{b:<10.6f}{c:<10.6f}{fc:<10.6f}")
        
        # Check if we found the root or the interval is small enough
        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            print(f"\nRoot found: {c} (after {i+1} iterations)")
            return c
        
        # Update the interval
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    print("\nMaximum iterations reached without finding the root.")
    return None

# User input for the function, interval, and tolerance
print("Welcome to the Bisection Method program!")
function = input("Enter the function f(x): ")  # Example: x**3 - x - 2
a = float(input("Enter the starting point of the interval (a): "))
b = float(input("Enter the ending point of the interval (b): "))
tolerance = float(input("Enter the tolerance (e.g., 1e-6): "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Run the Bisection Method
root = bisection_method(a, b, tolerance, max_iterations)
