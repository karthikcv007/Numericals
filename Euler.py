def f(x, y):
    # Define the ODE here, e.g., dy/dx = x + y
    return x + y

def euler_method(x0, y0, h, xn):
    steps = int((xn - x0) / h)
    x = x0
    y = y0

    print(f"{'Step':<5} {'x':<10} {'y':<10}")
    print(f"{0:<5} {x:<10.4f} {y:<10.4f}")

    for i in range(1, steps + 1):
        y = y + h * f(x, y)
        x = x + h
        print(f"{i:<5} {x:<10.4f} {y:<10.4f}")

    return y

# User Input
x0 = float(input("Enter initial x (x0): "))
y0 = float(input("Enter initial y (y0): "))
h = float(input("Enter step size h: "))
xn = float(input("Enter the value of x at which y is required: "))

result = euler_method(x0, y0, h, xn)
print(f"\nApproximate value of y at x = {xn} is {result:.4f}")
