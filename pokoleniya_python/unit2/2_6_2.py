from math import sqrt


def solve(a: int, b: int, c: int) -> set[float]:
    roots: set[float] = set()
    D = b * b - 4 * a * c
    if D < 0:
        return roots
    sqrt_D = sqrt(D)
    denom = 2 * a
    x1 = (-b - sqrt_D) / denom
    x2 = (-b + sqrt_D) / denom
    roots.add(x1)
    roots.add(x2)
    return roots
