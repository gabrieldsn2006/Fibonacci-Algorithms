def multiply_matrices(A: list, B: list) -> list:
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

def matrix_exponentiation(A: list, n: int) -> list:
    if n == 1:
        return A
    if n % 2 == 0:
        half_power = matrix_exponentiation(A, n // 2)
        return multiply_matrices(half_power, half_power)
    else:
        return multiply_matrices(A, matrix_exponentiation(A, n-1))

def fibonacci(n: int) -> int:
    if n <= 0: return 0
    if n <= 2: return 1
    A = [[1, 1], [1, 0]]
    result = matrix_exponentiation(A, n-1)
    return result[0][0]