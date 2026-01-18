# Matrix Operations Tool using NumPy
# Beginner friendly project

import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

print("=== MATRIX OPERATIONS TOOL ===")

A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

print("""
Choose Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Transpose of A
5. Determinant of A
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result (A + B):\n", A + B)

elif choice == 2:
    print("Result (A - B):\n", A - B)

elif choice == 3:
    print("Result (A x B):\n", np.dot(A, B))

elif choice == 4:
    print("Transpose of A:\n", A.T)

elif choice == 5:
    if A.shape[0] == A.shape[1]:
        print("Determinant of A:", np.linalg.det(A))
    else:
        print("Determinant not possible (Matrix not square)")

else:
    print("Invalid choice")
