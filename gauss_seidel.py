
import numpy as np

def gauss_seidel(A, b, x0, max_iterations=100):
    n = len(b)
    x = np.array(x0, dtype=float)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        print(f"Iteration {iteration + 1}:")
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
            print(f"  x[{i}] = {x_new[i]:.6f}")
        
        x = x_new
    
    print("Max iterations reached.")
    return x, max_iterations

# User input
def get_user_input():
    n = int(input("Enter the number of equations: "))
    A = []
    b = []
    print("Enter the coefficients of the equations:")
    for i in range(n):
        row = list(map(float, input(f"Equation {i+1}: ").split()))
        A.append(row[:-1])
        b.append(row[-1])
    
    x0 = list(map(float, input("Enter initial guesses separated by space: ").split()))
    
    return np.array(A), np.array(b), np.array(x0)

if __name__ == "__main__":
    A, b, x0 = get_user_input()
    solution, iterations = gauss_seidel(A, b, x0)
    print("Solution:", solution)
    print("Iterations:", iterations)
