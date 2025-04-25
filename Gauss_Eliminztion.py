def gauss_elimination_pivot(a, b):
    n = len(b)

    # Forward elimination with partial pivoting
    for i in range(n):
        # Partial Pivoting
        max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
        if i != max_row:
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]

        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]

    return x

# User input
n = int(input("Enter number of variables: "))
a = []
b = []

print("Enter the coefficients row by row:")
for i in range(n):
    row = list(map(float, input(f"Row {i + 1} (space-separated): ").split()))
    a.append(row[:-1])
    b.append(row[-1])

solution = gauss_elimination_pivot(a, b)
print("Solution:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.4f}")
