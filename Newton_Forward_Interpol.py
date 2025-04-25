def newton_forward_interpolation(x, y, value):
    n = len(x)
    # Create finite difference table
    diff_table = [y[:]]
    for i in range(1, n):
        new_row = [diff_table[i-1][j+1] - diff_table[i-1][j] for j in range(n - i)]
        diff_table.append(new_row)

    # h is the interval (assumes equally spaced x values)
    h = x[1] - x[0]
    u = (value - x[0]) / h

    # Calculate interpolation value
    result = y[0]
    u_term = 1
    fact = 1
    for i in range(1, n):
        u_term *= (u - i + 1)
        fact *= i
        result += (u_term * diff_table[i][0]) / fact

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

interpolated = newton_forward_interpolation(x, y, value)
print(f"Interpolated value at x = {value} is {interpolated:.4f}")
