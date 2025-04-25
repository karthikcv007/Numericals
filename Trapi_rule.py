def f(x):
    # Define the function to integrate here
    return x**2  # Example: f(x) = x^2

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]
    for i in range(1, n):
        result += 2 * y[i]

    result *= h / 2
    return result

# User input
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of intervals: "))

result = trapezoidal_rule(a, b, n)
print(f"Approximate integral using Trapezoidal Rule: {result:.4f}")
