import sys
import numpy as np

A = np.arange(1,5).reshape(2,2)

B = np.arange(5,9).reshape(2,2)

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