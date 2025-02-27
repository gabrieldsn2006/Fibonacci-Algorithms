def fibonacci(n: int) -> int:
    SQRT_FIVE = 5 ** (1/2)
    PHI = (1 + SQRT_FIVE) / 2
    PSI = (1 - SQRT_FIVE) / 2
    return int( (PHI ** n - PSI ** n) / SQRT_FIVE )