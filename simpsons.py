def f(x):
    # Define the function to integrate here
    return x**2  # Example: f(x) = x^2

def simpsons_rule(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3rd Rule")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * y[i]
        else:
            result += 4 * y[i]

    result *= h / 3
    return result

# User input
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of intervals (even number): "))

try:
    result = simpsons_rule(a, b, n)
    print(f"Approximate integral using Simpson's 1/3rd Rule: {result:.4f}")
except ValueError as e:
    print(e)
