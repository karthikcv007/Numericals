import numpy as np

def gauss_jordan(A, b):
    # Create augmented matrix by combining A and b
    n = len(b)
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])

    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Find the pivot element
        pivot = augmented_matrix[i, i]
        if pivot == 0:
            # Swap with a row below if the pivot is 0
            for j in range(i + 1, n):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    pivot = augmented_matrix[i, i]
                    break
        # Scale the pivot row to make the pivot equal to 1
        augmented_matrix[i] = augmented_matrix[i] / pivot
        
        # Eliminate the entries below and above the pivot in column i
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

    # The result is now in the last column of the augmented matrix
    return augmented_matrix[:, -1]

# Get the size of the matrix (number of equations/variables)
n = int(input("Enter the number of variables (or equations): "))

# Input the coefficient matrix A
print(f"Enter the coefficients of the {n} variables, one row at a time (separate by spaces):")
A = np.array([list(map(float, input().split())) for _ in range(n)])

# Input the constants matrix b
print("Enter the constants (right-hand side values):")
b = np.array([float(input()) for _ in range(n)])

# Call the Gauss-Jordan method to solve the system
solution = gauss_jordan(A, b)

# Display the solution
print("Solution: ", solution)
