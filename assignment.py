import sys
import numpy as np

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6],[7, 8]])

addition = A + B

multiplication = A * B

matrix_product = A @ B

def main():

    print(f"Array A: {A}")
    print(f"Array B: {B}")
    print(f"Elementwise Addition: {addition}")
    print(f"Elementwise Multiplication: {multiplication}")
    print(f"Matrix Product: {matrix_product}")
    return 0

if __name__ == "__main__":
    sys.exit(main())