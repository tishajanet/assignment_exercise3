import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

add_result = A + B

# Elementwise multiplication
mul_result = A * B

# Matrix product
matmul_result = A @ B   # or np.matmul(A, B)

print("Array A:\n", A)
print("Array B:\n", B)
print("\nElementwise Addition:\n", add_result)
print("\nElementwise Multiplication:\n", mul_result)
print("\nMatrix Product (A @ B):\n", matmul_result)
