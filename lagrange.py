def lagrange_interpolation(x, y, value):
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term

    return result

# User Input
n = int(input("Enter number of data points: "))
x = []
y = []

print("Enter x and y values:")
for i in range(n):
    xi, yi = map(float, input(f"Point {i+1} (x y): ").split())
    x.append(xi)
    y.append(yi)

value = float(input("Enter the value to interpolate: "))

interpolated = lagrange_interpolation(x, y, value)
print(f"Interpolated value at x = {value} is {interpolated:.4f}")
